FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --assume-yes apt-utils
RUN apt-get update && apt-get install -y git python3>=3.6 python3-pip

RUN cd /tmp \
  && git clone https://github.com/xjtu-omics/msisensor-rna.git \
  && cd msisensor-rna \
  && pip3 install . \
  && cp -r /usr/local/bin/msisensor-rna /usr/bin/