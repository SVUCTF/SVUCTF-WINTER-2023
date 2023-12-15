FROM ghcr.io/svuctf/base/php:latest as builder

COPY tonyenc /tonyenc
WORKDIR /tonyenc

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk add autoconf gcc make musl-dev --no-cache && \
    phpize && ./configure --with-config-file-path=/usr/local/etc/php/conf.d/ && \
    make && make install

COPY php.ini /usr/local/etc/php/conf.d/php.ini
COPY html /html

RUN php tonyenc.php /html

FROM ghcr.io/svuctf/base/php:latest

COPY php.ini /usr/local/etc/php/conf.d/php.ini
COPY --from=builder /tonyenc/modules/tonyenc.so /usr/local/lib/php/extensions/no-debug-non-zts-20220829/tonyenc.so
COPY --from=builder --chown=www-data  /html /var/www/html

COPY --chmod=500 init.sh /init.sh
