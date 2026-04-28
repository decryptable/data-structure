#Requires -Version 5.1
$ErrorActionPreference = "Stop"

$exePath = Join-Path $PSScriptRoot "data-structure.exe"

if (-not (Test-Path $exePath)) {
    Write-Error "Executable tidak ditemukan: $exePath"
    exit 1
}

& $exePath @args
