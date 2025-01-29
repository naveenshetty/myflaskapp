#!/bin/bash
set -e

# Stop the running container (if any)
# shellcheck disable=SC2016
# shellcheck disable=SC1068
containerID = docker ps | awk-F " " '{print $1}'

# shellcheck disable=SC2154
docker rm -f "$containerID"

