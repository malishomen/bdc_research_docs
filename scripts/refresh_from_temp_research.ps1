param(
    [string]$SourceRoot = 'D:\projects\Bio_Digital_Core\Temp\research',
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

function Sync-Tree {
    param(
        [string]$Source,
        [string]$Destination
    )
    if (-not (Test-Path $Source)) {
        Write-Host "SKIP missing: $Source"
        return
    }
    New-Item -ItemType Directory -Force $Destination | Out-Null
    robocopy $Source $Destination /MIR /R:1 /W:1 /NFL /NDL /NJH /NJS /NP | Out-Null
    $code = $LASTEXITCODE
    if ($code -ge 8) {
        throw "robocopy failed for $Source -> $Destination with exit code $code"
    }
    Write-Host "SYNC $Source -> $Destination"
}

$indexDir = Join-Path $RepoRoot '00_indexes'
$scientificDir = Join-Path $RepoRoot '10_scientific_line\BDC_MAIN_F'
$designerDir = Join-Path $RepoRoot '20_bdc_designer\BDC_Designer_F'
$externalDir = Join-Path $RepoRoot '30_external_sources\external'
$archiveDir = Join-Path $RepoRoot '90_archive'
$dissertationDir = Join-Path $RepoRoot '40_dissertation\Dissertation'

New-Item -ItemType Directory -Force $indexDir, $scientificDir, $designerDir, $externalDir, $archiveDir, $dissertationDir | Out-Null

Sync-Tree -Source (Join-Path $SourceRoot 'BDC_MAIN_F') -Destination $scientificDir
Sync-Tree -Source (Join-Path $SourceRoot 'BDC_Designer_F') -Destination $designerDir
Sync-Tree -Source (Join-Path $SourceRoot 'external') -Destination $externalDir

$archiveSources = @('internal', 'temp_works')
foreach ($name in $archiveSources) {
    Sync-Tree -Source (Join-Path $SourceRoot $name) -Destination (Join-Path $archiveDir $name)
}

Get-ChildItem $SourceRoot -Directory -Filter 'project_documentation_snapshot_*' -ErrorAction SilentlyContinue | ForEach-Object {
    Sync-Tree -Source $_.FullName -Destination (Join-Path $archiveDir $_.Name)
}

$summaryFiles = @(
    'BDC_EXTERNAL_RESEARCH_APPLICABILITY_REPORT.md',
    'BDC_PROJECT_GOALS_HYPOTHESES_AND_THEORIES.md',
    'BDC_PROJECT_GOALS_HYPOTHESES_AND_THEORIES_RU.md'
)
foreach ($file in $summaryFiles) {
    $src = Join-Path $SourceRoot $file
    if (Test-Path $src) {
        Copy-Item $src (Join-Path $indexDir $file) -Force
        Write-Host "COPY $src -> $indexDir"
    }
}

$dissertationFiles = @(
    'bdc_dissertation_draft.md',
    'bdc_dissertation_extended_draft.md',
    'bdc_dissertation_extended_draft.pre_cleanup_backup.md',
    'bdc_dissertation_omitted_materials_map.md'
)
foreach ($file in $dissertationFiles) {
    $src = Join-Path $SourceRoot $file
    if (Test-Path $src) {
        Copy-Item $src (Join-Path $dissertationDir $file) -Force
        Write-Host "COPY $src -> $dissertationDir"
    }
}

Write-Host 'Refresh complete. Review git status, then commit and push.'
