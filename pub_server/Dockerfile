FROM alpine:latest
MAINTAINER German Blanco

RUN apk add --update \
      python musl-dev python-dev gcc mysql-client mariadb-dev  \
      py-pip g++ libzmq  && \
      pip install --upgrade pip && \
      pip install MySQL-python pyzmq

ADD files/pub_server.py /root/code.py
ADD files/start.sh /root/start.sh

RUN chmod +x /root/code.py
RUN chmod +x /root/start.sh

ENTRYPOINT ["/root/start.sh"]
