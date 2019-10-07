FROM alpine

RUN apk update
RUN apk add python3

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD python3 pub.py
