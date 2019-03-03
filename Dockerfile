FROM python:3.6-alpine

LABEL maintainer="Peng Xiao <xiaoquwl@gmail.com>"

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

COPY . /twittor

WORKDIR /twittor

RUN pip install -r requirements.txt && pip install gunicorn&&chmod 755 run_server.sh

EXPOSE 8000

ENTRYPOINT [ "./run_server.sh" ]
