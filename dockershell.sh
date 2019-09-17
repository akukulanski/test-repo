#!/bin/bash
#docker run -it docker_image
docker run -v $(pwd):/home/ -w /home -it $1 /bin/bash -c $2
