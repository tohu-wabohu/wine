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

  mysql:
    image: mysql:8.0
    build:
      context: /data/build
      dockerfile: Dockerfile-mysql

  ubuntu:
    image: ubuntu:20.04
    command: sleep infinity
```
