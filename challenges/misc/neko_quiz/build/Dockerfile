FROM alpine:latest

COPY neko-quiz-server /app/neko-quiz-server
COPY questions.json /app/questions.json
COPY dist/ /app/dist/
COPY --chmod=500 init.sh /etc/init.sh

CMD ["/etc/init.sh"]
