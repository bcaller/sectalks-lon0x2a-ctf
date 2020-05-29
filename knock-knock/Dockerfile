# https://github.com/aristarkh87/docker-knockd

FROM ubuntu

RUN apt-get update && apt-get install -y \
        knockd \
        xinetd \
      && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
COPY knockd.conf /etc/knockd.conf
COPY xinetd.conf /etc/xinetd.d/flag
COPY flag.sh /flag.sh
COPY open61217.sh /open61217.sh
COPY close.sh /close.sh

CMD ["/entrypoint.sh"]
