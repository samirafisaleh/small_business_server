#!/bin/bash

service=mongodb_exporter

# Pushing the correct diretory
pushd ../../

source configurations/common.env

name="${APP_NAME}_${service}"

if [ ! "$(docker ps -a -q -f name=^$name$)" ]; 
then 

    major=$MONGODB_EXPORTER_MAJ
    minor=$MONGODB_EXPORTER_MIN
    patch=$MONGODB_EXPORTER_MAJ
    reltype=$MONGODB_EXPORTER_RELTYPE
    


    network="${project}_network"
    echo Network $network: Creating 
    docker network create $network

    echo $name: Starting
    docker run -d \
            -p 7216:9216 \
           --network $network \
           --name $name $name:$reltype-$major.$minor.$patch \
           --mongodb.uri=mongodb://chess_mongodb:27017 --compatible-mode
else 
    echo $name: Restarting
    docker restart $name
fi 

