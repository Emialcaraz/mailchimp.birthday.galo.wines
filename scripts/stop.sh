#!/bin/bash

export NETWORK_NAME=mailchimp

# Stop the project
docker-compose -f docker/docker-compose-dev.yml down
echo "The project is stopped!"
