param(
    [string]$OutRoot = "results/selection_physics_reboot_r1_full",
    [string]$OutJson = "results/selection_physics_reboot_r1_full/parallel_launch/progress_status.json"
)

$ErrorActionPreference = "Stop"

$resolvedOutRoot = [System.IO.Path]::GetFullPath($OutRoot)
$launchRoot = Join-Path $resolvedOutRoot "parallel_launch"
$startedPath = Join-Path $launchRoot "started_processes.json"
$manifestRoot = Join-Path $launchRoot "manifests"

if (-not (Test-Path $startedPath)) {
    throw "Missing started_processes.json: $startedPath"
}

$started = Get-Content -Raw $startedPath | ConvertFrom-Json
$workerManifests = Get-ChildItem -Path $manifestRoot -Filter "worker_*.json" | Sort-Object Name
if (-not $workerManifests) {
    throw "Missing worker manifests in: $manifestRoot"
}

$workers = @()
$completedRuns = 0
$totalRuns = 0
$elapsedSamples = @()
$activeRunSlots = 0

foreach ($manifestFile in $workerManifests) {
    $manifest = Get-Content -Raw $manifestFile.FullName | ConvertFrom-Json
    $workerId = [string]$manifest.parallel_worker_id
    $workerOutRoot = Join-Path $resolvedOutRoot ("worker_{0}" -f $workerId)
    $expectedRuns = @($manifest.genome_versions).Count * @($manifest.selection_regimes).Count * @($manifest.seeds).Count
    $summaryFiles = @(Get-ChildItem -Path $workerOutRoot -Filter "summary.json" -Recurse -ErrorAction SilentlyContinue)
    $metricsFiles = @(Get-ChildItem -Path $workerOutRoot -Filter "metrics.csv" -Recurse -ErrorAction SilentlyContinue)
    $completedWorkerRuns = [Math]::Min($summaryFiles.Count, $metricsFiles.Count)
    $activeWorkerSlots = @(
        $metricsFiles |
        Where-Object { $_.Length -ge 0 } |
        Select-Object -ExpandProperty DirectoryName -Unique
    ).Count

    $workerStarted = $started | Where-Object { $_.worker_id -eq $workerId } | Select-Object -First 1
    $workerPid = $null
    $startTime = $null
    $isRunning = $false
    if ($workerStarted) {
        $workerPid = [int]$workerStarted.pid
        $proc = Get-Process -Id $workerPid -ErrorAction SilentlyContinue
        if ($proc) {
            $isRunning = $true
            $startTime = $proc.StartTime
        }
    }

    $completedRuns += $completedWorkerRuns
    $totalRuns += $expectedRuns
    $activeRunSlots += $activeWorkerSlots
    if ($startTime -and $completedWorkerRuns -gt 0) {
        $elapsedHours = ((Get-Date) - $startTime).TotalHours
        if ($elapsedHours -gt 0) {
            $elapsedSamples += [pscustomobject]@{
                completed = $completedWorkerRuns
                elapsed_hours = $elapsedHours
            }
        }
    }

    $workers += [pscustomobject]@{
        worker_id = $workerId
        pid = $workerPid
        running = $isRunning
        expected_runs = $expectedRuns
        completed_runs = $completedWorkerRuns
        active_run_slots = $activeWorkerSlots
        selection_regimes = @($manifest.selection_regimes)
    }
}

$percentComplete = 0.0
if ($totalRuns -gt 0) {
    $percentComplete = [Math]::Round(($completedRuns / $totalRuns) * 100.0, 2)
}

$etaHours = $null
if ($completedRuns -gt 0 -and $elapsedSamples.Count -gt 0) {
    $totalElapsedHours = ($elapsedSamples | Measure-Object -Property elapsed_hours -Sum).Sum
    if ($totalElapsedHours -gt 0) {
        $runRate = $completedRuns / $totalElapsedHours
        if ($runRate -gt 0) {
            $remainingRuns = $totalRuns - $completedRuns
            $etaHours = [Math]::Round($remainingRuns / $runRate, 2)
        }
    }
}

$payload = [ordered]@{
    collected_at_utc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    out_root = $resolvedOutRoot
    total_runs = $totalRuns
    completed_runs = $completedRuns
    active_run_slots = $activeRunSlots
    percent_complete = $percentComplete
    eta_hours = $etaHours
    eta_hint = if ($etaHours -eq $null -and $completedRuns -eq 0 -and $activeRunSlots -gt 0) {
        "waiting_for_first_completed_run; expected_total_runtime_hours_on_this_host_approx=4-6"
    } else {
        $null
    }
    workers = $workers
}

$outDir = Split-Path -Parent $OutJson
if ($outDir) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}
$payload | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $OutJson
$payload | ConvertTo-Json -Depth 6 | Write-Output
