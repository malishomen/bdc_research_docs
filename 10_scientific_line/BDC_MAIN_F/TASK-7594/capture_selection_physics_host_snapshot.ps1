param(
    [string]$OutJson = "reports/analysis/TASK-7594-BDC-SELECTION-PHYSICS-R1-LAUNCH-PREP/host_snapshot.json"
)

$ErrorActionPreference = "Stop"

$cpuInfo = Get-CimInstance Win32_Processor
$logicalCpu = ($cpuInfo | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
$cpuTotal = Get-CimInstance Win32_PerfFormattedData_PerfOS_Processor | Where-Object { $_.Name -eq "_Total" }
$osInfo = Get-CimInstance Win32_OperatingSystem

$gpuInfo = $null
try {
    $gpuCsv = & nvidia-smi --query-gpu=name,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu --format=csv,noheader
    $gpuInfo = @()
    foreach ($line in $gpuCsv) {
        $parts = $line -split ", "
        if ($parts.Count -ge 6) {
            $gpuInfo += [pscustomobject]@{
                name = $parts[0]
                utilization_gpu = $parts[1]
                utilization_memory = $parts[2]
                memory_used = $parts[3]
                memory_total = $parts[4]
                temperature_gpu = $parts[5]
            }
        }
    }
} catch {
    $gpuInfo = @()
}

$topProcesses = Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 20 Id, ProcessName, CPU,
        @{Name="WS_MB";Expression={[math]::Round($_.WS / 1MB, 1)}},
        @{Name="PM_MB";Expression={[math]::Round($_.PM / 1MB, 1)}},
        StartTime

$pythonProcesses = Get-Process python -ErrorAction SilentlyContinue |
    Select-Object Id, ProcessName, CPU,
        @{Name="WS_MB";Expression={[math]::Round($_.WS / 1MB, 1)}},
        @{Name="PM_MB";Expression={[math]::Round($_.PM / 1MB, 1)}},
        StartTime, Path

$payload = [ordered]@{
    collected_at_utc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    logical_cpu = $logicalCpu
    total_cpu_percent = $cpuTotal.PercentProcessorTime
    free_memory_mb = [math]::Round(($osInfo.FreePhysicalMemory / 1024), 1)
    gpu = $gpuInfo
    python_process_count = @($pythonProcesses).Count
    python_processes = $pythonProcesses
    top_processes = $topProcesses
}

$outDir = Split-Path -Parent $OutJson
if ($outDir) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}
$payload | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $OutJson
Write-Output $OutJson
