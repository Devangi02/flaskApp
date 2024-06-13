#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull demorepo123/demo-flask-application

# Run the Docker image as a container
docker run -d -p 8080:8000 demorepo123/demo-flask-application 
