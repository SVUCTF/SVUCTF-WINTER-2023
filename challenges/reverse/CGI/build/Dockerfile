FROM alpine as builder

COPY main.c /main.c

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk add musl-dev gcc --no-cache && \
    gcc main.c -o challenge.cgi

FROM httpd:alpine

COPY httpd.conf conf/httpd.conf
COPY --from=builder --chmod=0544 --chown=www-data challenge.cgi cgi-bin/challenge.cgi
COPY --chmod=0544 init.sh /init.sh

CMD ["/init.sh"]
