#!/bin/bash

service=redis_insight

# Pushing the correct diretory
pushd ../../

source configurations/common.env

name="${APP_NAME}_${service}"

if [ ! "$(docker ps -a -q -f name=^$name$)" ]; 
then 
    major=$REDIS_INSIGHT_MAJ
    minor=$REDIS_INSIGHT_MIN
    patch=$REDIS_INSIGHT_PAT
    reltype=$REDIS_INSIGHT_RELTYPE

    volume="${project}_volume_redis_insight"
    echo Volume $volume: Creating
    docker volume create $volume

    network="${project}_network"
    echo Network $network: Creating 
    docker network create $network

    echo $name: Starting
    docker run -d -p 7540:5540 \
           --network $network \
           -v $volume:/data \
           --name $name $name:$reltype-$major.$minor.$patch
else 
    echo $name: Restarting
    docker restart $name
fi 

