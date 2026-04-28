#!/bin/bash

# Activate the virtual environment
# We use 'source' to make sure the environment stays active for the next command
source venv/bin/activate

# Execute the test suite
# Pytest automatically returns the exit code we need: 
# 0 for success, non-zero for failure.
pytest test_app.py

# Capture the exit code of the last command (pytest)
test_status=$?

# Return the exit code
if [ $test_status -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed. Check the logs above."
    exit 1
fi