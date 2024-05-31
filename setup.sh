#!/bin/bash

# Set up project and install upstream requirements

python3 -m venv venv
# shellcheck source=/dev/null  # don't check venv activate script
source venv/bin/activate
pip install -r requirements.txt
