#!/bin/bash

if [ -n "$DOCKER_PASSWORD" ]; then
  if [ -n "$DOCKER_USERNAME" ]; then
    echo "Pushing docker img"
    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
  else
    echo "DOCKER_USERNAME not set."
    exit -1
  fi
else
  echo "DOCKER_PASSWORD not set."
  exit -2
fi

