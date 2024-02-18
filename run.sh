#!/bin/bash

# Check if a filename argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide the name of the file to serve."
    exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found."
    exit 1
fi

# Set the environment variable for the file name
export TEXT_FILE_NAME=$1

chmod +x ./build.sh

# Call build.sh
./build.sh
