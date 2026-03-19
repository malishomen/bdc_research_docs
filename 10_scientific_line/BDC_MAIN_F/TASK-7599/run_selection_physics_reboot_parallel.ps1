param(
    [string]$ManifestPath = "scripts/edp1/selection_physics_manifest.json",
    [string]$OutRoot = "results/selection_physics_reboot_r1_full",
    [string]$PythonExe = "python",
    [int]$WorkerCount = 4,
    [switch]$Execute
)

$ErrorActionPreference = "Stop"
$Utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Split-Regimes {
    param(
        [string[]]$Regimes,
        [int]$Buckets
    )
    $bucketCount = [Math]::Min([Math]::Max(1, $Buckets), $Regimes.Count)
    $groups = @()
    for ($i = 0; $i -lt $bucketCount; $i++) {
        $groups += ,@()
    }
    for ($i = 0; $i -lt $Regimes.Count; $i++) {
        $bucketIndex = $i % $bucketCount
        $groups[$bucketIndex] += $Regimes[$i]
    }
    return $groups
}

$manifest = Get-Content $ManifestPath | ConvertFrom-Json
$resolvedOutRoot = [System.IO.Path]::GetFullPath($OutRoot)
$launchRoot = Join-Path $resolvedOutRoot "parallel_launch"
$manifestOut = Join-Path $launchRoot "manifests"
$logOut = Join-Path $launchRoot "logs"
New-Item -ItemType Directory -Force -Path $manifestOut | Out-Null
New-Item -ItemType Directory -Force -Path $logOut | Out-Null

$groups = Split-Regimes -Regimes ([string[]]$manifest.selection_regimes) -Buckets $WorkerCount
$launchPlan = @()

for ($i = 0; $i -lt $groups.Count; $i++) {
    $workerId = "{0:d2}" -f ($i + 1)
    $workerManifestPath = Join-Path $manifestOut ("worker_{0}.json" -f $workerId)
    $workerOutRoot = Join-Path $resolvedOutRoot ("worker_{0}" -f $workerId)

    $workerManifest = [ordered]@{
        task = $manifest.task
        description = $manifest.description
        task_environment = $manifest.task_environment
        genome_versions = $manifest.genome_versions
        selection_regimes = $groups[$i]
        seeds = $manifest.seeds
        runner_defaults = $manifest.runner_defaults
        generated_for_parallel_launch = $true
        parallel_worker_id = $workerId
        base_manifest_path = [System.IO.Path]::GetFullPath($ManifestPath)
    }
    [System.IO.File]::WriteAllText(
        $workerManifestPath,
        ($workerManifest | ConvertTo-Json -Depth 8),
        $Utf8NoBom
    )

    $argList = @(
        "scripts/edp1/run_selection_physics_reboot_sweep.py",
        "--manifest", $workerManifestPath,
        "--out_root", $workerOutRoot
    )
    $stdoutPath = Join-Path $logOut ("worker_{0}_stdout.log" -f $workerId)
    $stderrPath = Join-Path $logOut ("worker_{0}_stderr.log" -f $workerId)

    $launchPlan += [pscustomobject]@{
        worker_id = $workerId
        regimes = ($groups[$i] -join ",")
        manifest_path = $workerManifestPath
        out_root = $workerOutRoot
        stdout_path = $stdoutPath
        stderr_path = $stderrPath
        command = "$PythonExe $($argList -join ' ')"
    }
}

$planPath = Join-Path $launchRoot "launch_plan.json"
[System.IO.File]::WriteAllText(
    $planPath,
    ($launchPlan | ConvertTo-Json -Depth 6),
    $Utf8NoBom
)

if (-not $Execute) {
    Write-Output "PREVIEW_ONLY"
    Write-Output ("PLAN=" + $planPath)
    $launchPlan | Format-Table -AutoSize | Out-String | Write-Output
    exit 0
}

$started = @()
foreach ($item in $launchPlan) {
    $proc = Start-Process -FilePath $PythonExe -ArgumentList @(
        "scripts/edp1/run_selection_physics_reboot_sweep.py",
        "--manifest", $item.manifest_path,
        "--out_root", $item.out_root
    ) -RedirectStandardOutput $item.stdout_path -RedirectStandardError $item.stderr_path -PassThru

    $started += [pscustomobject]@{
        worker_id = $item.worker_id
        pid = $proc.Id
        manifest_path = $item.manifest_path
        out_root = $item.out_root
        stdout_path = $item.stdout_path
        stderr_path = $item.stderr_path
    }
}

$startedPath = Join-Path $launchRoot "started_processes.json"
[System.IO.File]::WriteAllText(
    $startedPath,
    ($started | ConvertTo-Json -Depth 6),
    $Utf8NoBom
)
Write-Output ("STARTED=" + $startedPath)
