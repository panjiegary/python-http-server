FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
    python3 \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN cd ~ && git clone https://github.com/panjiegary/python-http-server.git && cd python-http-server && python3 server.py