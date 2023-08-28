#!/bin/sh

DOCKER_BUILDKIT=1 docker build --target=runtime -t immich-carddav-sync .
