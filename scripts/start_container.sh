#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull demorepo123/demo-flask-application

# Run the Docker image as a container
docker run -d -p 80:8080 Devangi02/flaskApp
