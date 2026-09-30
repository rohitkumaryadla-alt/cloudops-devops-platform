#!/bin/bash

echo "Checking CloudOps API..."

response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)

if [ "$response" -eq 200 ]; then
    echo "CloudOps API is healthy."
    exit 0
else
    echo "CloudOps API health check failed. HTTP status: $response"
    exit 1
fi