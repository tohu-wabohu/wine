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
  python3 python3-pip
#  && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/wine
WORKDIR /opt/wine

RUN pip install Flask requests markdown

ADD app.py .

CMD python3 app.py
