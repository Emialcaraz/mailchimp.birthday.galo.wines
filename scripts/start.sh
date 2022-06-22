#!/bin/bash

export NETWORK_NAME=mailchimp

# Check for NETWORK_NAME network and create it
if [ -z $(docker network ls --filter name=^${NETWORK_NAME}$ --format="{{ .Name }}") ] ; then
    echo "Creating network '$NETWORK_NAME'"
    docker network create ${NETWORK_NAME} ;
fi

# If called with 'build', build the project first
if [[ "$1" == build ]]
then
    cd .. && docker-compose -f docker/docker-compose.yml build
fi


# If called with start, then the project is started
if [[ "$1" == start ]]
then
   docker run --network $NETWORK_NAME -it -v $(pwd)/../src:/usr/app --env-file $(pwd)/../docker/.env dwrk.slack.channel.creator python main.py
fi

pre-commit install
pre-commit install --install-hooks
