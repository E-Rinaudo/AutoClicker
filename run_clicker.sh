#!/bin/bash

# Activate venv from the script's directory.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/venv/bin/activate"

# Run with the venv python.
"${VIRTUAL_ENV:-$SCRIPT_DIR/venv}/bin/python" "${SCRIPT_DIR}/autoclicker.py"
