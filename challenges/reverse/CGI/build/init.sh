#!/usr/bin/env sh

echo "$GZCTF_FLAG" > /flag
chmod 444 /flag
unset GZCTF_FLAG

httpd -D FOREGROUND