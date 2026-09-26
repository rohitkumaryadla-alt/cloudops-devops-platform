#!/bin/bash

# 1. Activate the virtual environment
if [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

echo "Starting automated tests..."

# 2. Run pytest using python module
python -m pytest -v

if [ $? -ne 0 ]; then
    echo "Tests failed."
    exit 1
fi

echo "All tests passed."