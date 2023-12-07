FROM scratch

COPY neko-quiz /neko-quiz
COPY config.json /config.json
COPY dist/ /dist/

ENTRYPOINT ["/neko-quiz"]
CMD ["-a", "0.0.0.0"]
