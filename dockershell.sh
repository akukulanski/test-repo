#!/bin/bash
#docker run -it docker_image
docker run -v $(pwd):/home/ -w /home -it docker_image_2 /bin/bash -c $1
