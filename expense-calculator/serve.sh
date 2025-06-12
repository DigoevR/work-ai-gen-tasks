#!/bin/bash
# Serve the current directory using Python's built-in HTTP server

PORT=8000

if command -v python3 &> /dev/null; then
    echo "Serving on http://localhost:$PORT"
    python3 -m http.server $PORT
else
    echo "python3 is not installed. Please install Python 3 to use this script."
    exit 1
fi 