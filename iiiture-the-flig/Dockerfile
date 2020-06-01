# https://github.com/aristarkh87/docker-knockd

FROM ubuntu

RUN apt-get update && apt-get install -y \
        vim \
        telnetd \
        xinetd \
      && rm -rf /var/lib/apt/lists/*

RUN adduser --uid 1234 --gecos '' guest && \
    passwd -d guest

COPY xinetd.conf /etc/xinetd.d/vim
COPY vim.sh /bin/login
COPY telnet.sh /telnet.sh
COPY vimrc /home/guest/.vimrc
ARG VIM_FLAG
RUN chown -R root:root /home/guest && \
    echo $VIM_FLAG > /flag.txt

CMD ["/usr/sbin/xinetd", "-dontfork"]
