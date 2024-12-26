#!/bin/bash

service=grafana

# Pushing the correct diretory
pushd ../../

source configurations/common.env

name="${APP_NAME}_${service}"


if [ ! "$(docker ps -a -q -f name=^$name$)" ]; 
then

    major=$GRAFANA_MAJ
    minor=$GRAFANA_MIN
    patch=$GRAFANA_MAJ
    reltype=$GRAFANA_RELTYPE

    volume="${name}_volume_${service}"
    echo Volume $volume: Creating
    docker volume create $volume

    volume_conf="${name}_volume_${service}_conf"
    echo Volume $volume_conf: Creating
    docker volume create $volume_conf

    network="${APP_NAME}_network"
    echo Network $network: Creating 
    docker network create $network

    echo $name: Starting
    docker run -d -p 7001:3000 \
           --network $network \
           -v $volume:/var/log/grafana \
           -v $volume_conf:/etc/grafana \
           --name $name $name:$reltype-$major.$minor.$patch

else 
    echo $name: Copying grafana.ini
    docker cp configurations/grafana.ini chess_grafana:/etc/grafana/

    echo $name: Restarting
    docker restart $name
fi 



