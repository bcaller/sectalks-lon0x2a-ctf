FROM python:slim

RUN apt-get update && apt-get install -y \
        xinetd \
      && rm -rf /var/lib/apt/lists/*

RUN useradd guest

COPY xinetd.conf /etc/xinetd.d/redos
COPY run.sh /run.sh
COPY app.py /app.py

ENTRYPOINT ["/usr/sbin/xinetd", "-dontfork"]
