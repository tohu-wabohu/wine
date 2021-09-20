# Docker

Docker Compose, docker-compose.yml, example:
```
version: "2.2"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    mem_limit: 4g
    dns:
      - 8.8.8.8
      - 4.4.4.4

  # Set an alternative Dockerfile in docker-compose.yml
  mysql:
    image: mysql:8.0
    build:
      context: /data/build
      dockerfile: Dockerfile-mysql

  ubuntu:
    image: ubuntu:20.04
    command: sleep infinity
```

Dockerfile example:
```
FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  procps \
  iproute2 \
  dnsutils \
  iputils-ping \
  git \
  curl \
  wget \
  vim \
  # ---- other packages -----
  && rm -rf /var/lib/apt/lists/*
```

Join nodes to swarm - retrieve the join command including the join token:
```
docker swarm join-token worker                # as a worker node
docker swarm join-token manager               # as a manager node
```
