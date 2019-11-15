FROM ubuntu:18.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python3-pip


WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]