param(
    [switch]$Quiet
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$sourceSkill = Join-Path $repoRoot "review"

if (-not (Test-Path $sourceSkill)) {
    throw "Review source folder not found: $sourceSkill"
}

$codexHome = if ($env:CODEX_HOME) {
    $env:CODEX_HOME
} else {
    Join-Path $HOME ".codex"
}

$targetRoot = Join-Path $codexHome "skills"
$targetSkill = Join-Path $targetRoot "review"

if (-not (Test-Path $targetRoot)) {
    New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null
}

$null = robocopy $sourceSkill $targetSkill /MIR /NFL /NDL /NJH /NJS /NP
$robocopyExitCode = $LASTEXITCODE
if ($robocopyExitCode -gt 7) {
    throw "robocopy failed with exit code $robocopyExitCode"
}

$validator = Join-Path $codexHome "skills\.system\skill-creator\scripts\quick_validate.py"
if ((Test-Path $validator) -and (Get-Command python -ErrorAction SilentlyContinue)) {
    $null = python $validator $targetSkill
    if ($LASTEXITCODE -ne 0) {
        throw "Skill validation failed for $targetSkill"
    }
}

if (-not $Quiet) {
    Write-Host "Synced review skill to $targetSkill"
}
