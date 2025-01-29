#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull naveen192/myflaskapp:latest

# Run the Docker image as a container
docker run -d -p 8080:8080 naveen192/myflaskapp:latest