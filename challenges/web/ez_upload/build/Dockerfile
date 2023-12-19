FROM ghcr.io/svuctf/base/php:latest

COPY html/ /var/www/html/
RUN chown -R www-data:www-data /var/www/html/

COPY --chmod=500 init.sh /etc/init.sh

CMD ["/etc/init.sh"]
