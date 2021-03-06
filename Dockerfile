FROM alpine:3.5

ADD code.py /

ADD server.py /

ADD server.cfg /

ADD nikke.conf /

RUN apk update && apk add --no-cache python3 && pip3 install flask && pip3 install cherrypy

COPY code.py /src/code.py

EXPOSE 9209

CMD python3 server.py
