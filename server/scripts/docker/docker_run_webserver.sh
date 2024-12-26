#!/bin/bash

pushd ..

project=chess

name="${project}_webserver"

if [ ! "$(docker ps -a -q -f name=^$name$)" ]; 
then 

    volume="${project}_volume_webserver"
    echo Volume $volume: Creating
    docker volume create $volume

    network="${project}_network"
    echo Network $network: Creating 
    docker network create $network

    name="${project}_webserver"

    echo $name: Starting
    docker run --rm -d -p 7000:3000 \
            --network $network \
            -v $volume:/var/log/$project \
            --name $name $name:$reltype-$major.$minor.$patch

else 
    echo $name: Restarting
    docker restart $name
fi 

