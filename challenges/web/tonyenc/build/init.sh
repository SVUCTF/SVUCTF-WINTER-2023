#!/usr/bin/env sh

FLAG_FILE=$(mktemp -u "/flag_XXXXXXXX")
echo $GZCTF_FLAG > $FLAG_FILE
chmod 444 $FLAG_FILE

unset GZCTF_FLAG

php-fpm -D
nginx -g 'daemon off;'
