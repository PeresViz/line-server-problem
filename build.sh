#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application using uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
