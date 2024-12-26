#!/bin/bash

service=mongodb

# Pushing the correct diretory
pushd ../../

source configurations/common.env

name="${APP_NAME}_${service}"

if [ ! "$(docker ps -a -q -f name=^$name$)" ]; 
then
    major=$MONGODB_MAJ
    minor=$MONGODB_MIN
    patch=$MONGODB_MAJ
    reltype=$MONGODB_RELTYPE

    # volume="${project}_volume_redis"
    # echo Volume $volume: Creating
    # docker volume create $volume

    # volume_conf="${project}_volume_redis_conf"
    # echo Volume $volume_conf: Creating
    # docker volume create $volume_conf

    network="${project}_network"
    echo Network $network: Creating 
    docker network create $network

    echo $name: Starting
    docker run -d  \
            -p 7017:27017 \
            --network $network \
            --name $name $name:$reltype-$major.$minor.$patch

else 
    # echo $name: Copying redis.conf
    # docker cp configurations/redis.conf chess_redis:/usr/local/etc/redis/

    echo $name: Restarting
    docker restart $name
fi

