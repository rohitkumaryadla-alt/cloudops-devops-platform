Write-Host "Starting automated tests..."

python -m pytest -v

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed."
    exit 1
}

Write-Host "All tests passed."
exit 0