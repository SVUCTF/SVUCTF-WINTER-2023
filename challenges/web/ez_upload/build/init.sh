#!/bin/sh

echo $GZCTF_FLAG > /var/www/flag
chmod 444 /var/www/flag

unset GZCTF_FLAG

php-fpm -D
nginx -g 'daemon off;'
