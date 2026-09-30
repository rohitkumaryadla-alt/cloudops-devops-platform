$response = Invoke-WebRequest `
    -Uri "http://localhost:8000/health" `
    -UseBasicParsing

if ($response.StatusCode -eq 200) {
    Write-Host "CloudOps API is healthy."
    exit 0
}

Write-Host "CloudOps API health check failed."
exit 1