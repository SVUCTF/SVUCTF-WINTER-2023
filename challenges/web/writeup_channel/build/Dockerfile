FROM python:alpine

ENV FLASK_APP=app FLASK_ENV=production FLASK_ENV_DEBUG=False

RUN pip install flask gunicorn selenium --no-cache-dir && \
    sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update && apk add chromium-chromedriver --no-cache

COPY --chmod=500 init.sh /init.sh
COPY ./app /app
COPY ./bot /bot

CMD ["/init.sh"]
