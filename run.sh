#!/bin/sh -ev 
name=$(basename $PWD)
docker run -d  -p 11211:11211   --name=$name    -it    memcached:latest
#Run your Docker Image

