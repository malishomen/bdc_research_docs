param(
    [string]$CommitMessage = "Refresh research mirror",
    [switch]$SkipPush
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Push-Location $repoRoot
try {
    powershell -ExecutionPolicy Bypass -File .\scripts\refresh_from_temp_research.ps1
    git status --short
    git add -A
    $hasChanges = $false
    git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
        $hasChanges = $true
    }
    if (-not $hasChanges) {
        Write-Host 'No changes to commit.'
        exit 0
    }
    git commit -m $CommitMessage
    if (-not $SkipPush) {
        git push origin main
    }
}
finally {
    Pop-Location
}
