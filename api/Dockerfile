FROM ubuntu:20.04

LABEL maintainer="LSS"

ARG ROOT_USERNAME
ARG ROOT_PASSWORD
ARG IP_MONGODB

RUN apt-get update && apt-get upgrade -y && DEBIAN_FRONTEND="noninteractive" TZ="America/Sao_Paulo" apt-get install -y tzdata && apt-get install apache2 -y && apt-get install sed -y && apt-get clean

RUN apt-get install libapache2-mod-wsgi-py3 python3-dev libpq-dev python3-pip -y && a2enmod wsgi && pip3 install flask requests pymongo

RUN mkdir /home/api && cd /home/api && touch __init__.py

COPY api.py api.wsgi /home/api/
COPY api.conf /etc/apache2/sites-available/

RUN cd /etc/apache2/sites-available/ && rm 000-default.conf && a2ensite api.conf && service apache2 restart

RUN cd /home/api && sed -i "s/ROOT_USERNAME/$ROOT_USERNAME/" api.py && sed -i "s/ROOT_PASSWORD/$ROOT_PASSWORD/" api.py && sed -i "s/IP_MONGODB/$IP_MONGODB/" api.py 

EXPOSE 80
CMD apachectl -D FOREGROUND
