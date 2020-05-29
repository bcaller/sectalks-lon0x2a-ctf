FROM python:slim

RUN apt-get update && apt-get install -y \
        xinetd \
      && rm -rf /var/lib/apt/lists/*

RUN useradd guest

COPY xinetd.conf /etc/xinetd.d/ssrf
COPY run.py /run.py
COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
