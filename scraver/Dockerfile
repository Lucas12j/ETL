FROM ubuntu:20.04

LABEL maintainer="LSS"

RUN apt-get update && apt-get upgrade -y && DEBIAN_FRONTEND="noninteractive" TZ="America/Sao_Paulo" apt-get install -y tzdata && apt-get clean

RUN apt-get install firefox wget python3 python3-pip -y && pip3 install flask selenium==4.2.0 bs4 requests lxml

RUN mkdir /home/api && cd /home/api && mkdir scraper && cd scraper && touch __init__.py && mkdir /driver && touch /driver/geckodriver.log

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz && tar -xvzf geckodriver-v0.31.0-linux64.tar.gz && rm geckodriver-v0.31.0-linux64.tar.gz && chmod +x geckodriver && mv geckodriver /driver

COPY routes.py /home/api/
COPY scraperb.py scrapers.py /home/api/scraper/

EXPOSE 80

CMD ["python3", "/home/api/routes.py"]
