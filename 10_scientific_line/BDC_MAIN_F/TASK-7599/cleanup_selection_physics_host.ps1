param(
    [switch]$Execute,
    [string]$OutJson = "reports/analysis/TASK-7598-BDC-R1-CANONICAL-LAUNCH-PREP-AND-CLEANUP/cleanup_preview_2026-03-19.json"
)

$ErrorActionPreference = "Stop"

function Get-ProcessSnapshot {
    $processes = Get-CimInstance Win32_Process | Select-Object Name, ProcessId, CommandLine
    return $processes
}

function Match-Target {
    param(
        [object]$Process
    )

    $name = [string]$Process.Name
    $cmd = [string]$Process.CommandLine

    if ($name -match '^Codex(\.exe)?$') {
        return $false
    }

    if ($name -match '^pwsh(\.exe)?$' -or $name -match '^powershell(\.exe)?$') {
        if ($cmd -match 'cleanup_selection_physics_host\.ps1' -or $cmd -match 'Codex') {
            return $false
        }
    }

    $exactNames = @(
        'ChatGPT.exe',
        'claude.exe',
        'Telegram.exe',
        'com.docker.backend.exe',
        'docker.exe',
        'Code.exe'
    )
    if ($exactNames -contains $name) {
        return $true
    }

    if ($name -match '^node(\.exe)?$') {
        if ($cmd -match 'next dev' -or $cmd -match '@playwright/mcp' -or $cmd -match '\\next\\dist\\bin\\next') {
            return $true
        }
    }

    if ($name -match '^python(\.exe)?$') {
        if ($cmd -match 'pytest' -or $cmd -match 'jedilsp' -or $cmd -match 'jedi\\inference\\compiled\\subprocess') {
            return $true
        }
    }

    if ($name -match '^wslservice(\.exe)?$' -or $name -match '^vmmemWSL(\.exe)?$') {
        return $true
    }

    return $false
}

$snapshot = Get-ProcessSnapshot
$targets = @($snapshot | Where-Object { Match-Target $_ })

$targetPayload = foreach ($proc in $targets) {
    [pscustomobject]@{
        name = [string]$proc.Name
        process_id = [int]$proc.ProcessId
        command_line = [string]$proc.CommandLine
        action = if ($Execute.IsPresent) { "terminate" } else { "preview_only" }
    }
}

$terminated = @()
if ($Execute.IsPresent) {
    foreach ($proc in $targets) {
        try {
            Stop-Process -Id ([int]$proc.ProcessId) -Force -ErrorAction Stop
            $terminated += [pscustomobject]@{
                process_id = [int]$proc.ProcessId
                name = [string]$proc.Name
                terminated = $true
            }
        } catch {
            $terminated += [pscustomobject]@{
                process_id = [int]$proc.ProcessId
                name = [string]$proc.Name
                terminated = $false
                error = $_.Exception.Message
            }
        }
    }
}

$payload = [ordered]@{
    collected_at_utc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    execute = $Execute.IsPresent
    codex_protected = $true
    target_count = @($targetPayload).Count
    targets = $targetPayload
    terminated = $terminated
}

$outDir = Split-Path -Parent $OutJson
if ($outDir) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}
$payload | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $OutJson
Write-Output $OutJson
