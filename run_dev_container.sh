#! /bin/bash
docker run -it --entrypoint /bin/sh -p 127.0.0.1:10000:8080/tcp backend
