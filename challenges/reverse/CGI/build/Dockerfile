FROM httpd:alpine

COPY httpd.conf conf/httpd.conf
COPY --chmod=0544 --chown=www-data container.cgi cgi-bin/container.cgi
COPY --chmod=0544 init.sh /init.sh

CMD ["/init.sh"]