#!/bin/bash

export NETWORK_NAME=mailchimp

# Check for NETWORK_NAME network and create it
if [ -z $(docker network ls --filter name=^${NETWORK_NAME}$ --format="{{ .Name }}") ] ; then
    echo "Creating network '$NETWORK_NAME'"
    docker network create ${NETWORK_NAME} ;
fi

# If called with 'build', rebuild the project first
if [[ "$1" == build ]]
then
    echo "Building the project"
    docker-compose -f docker/docker-compose-dev.yml build
fi

# Start the project
docker-compose -f docker/docker-compose-dev.yml up -d
echo "The project is running!"
