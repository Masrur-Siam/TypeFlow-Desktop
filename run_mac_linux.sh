#!/bin/bash
echo "Installing dependencies..."
pip3 install -r requirements.txt
echo "Starting TypeFlow..."
python3 app.py