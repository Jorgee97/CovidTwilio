FROM python:3.8-slim

RUN    apt-get update \
&& apt-get install openssl \
&& apt-get install ca-certificates

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD gunicorn --timeout 1000 -b :5000 --workers=4 --threads=4 wsgi:app
