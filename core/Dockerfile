FROM alpine

LABEL maintainer="LSS"

ARG ROOT_USERNAME
ARG ROOT_PASSWORD
ARG IP_MONGODB
ARG IP_SCRAVER

RUN apk update && apk upgrade && apk add python3 && apk add py3-pip && apk add sed
RUN apk add tzdata && cp /usr/share/zoneinfo/Brazil/East /etc/localtime
RUN pip install pymongo requests

COPY crontab.txt /crontab.txt
COPY job.sh /home/job.sh
COPY entry.sh /entry.sh
COPY core.py /home/core.py
COPY parameters.json /home/parameters.json
RUN chmod +x /home/job.sh /entry.sh
RUN /usr/bin/crontab /crontab.txt

RUN cd /home && sed -i "s/ROOT_USERNAME/$ROOT_USERNAME/" parameters.json && sed -i "s/ROOT_PASSWORD/$ROOT_PASSWORD/" parameters.json && sed -i "s/IP_MONGODB/$IP_MONGODB/" parameters.json && sed -i "s/IP_SCRAVER/$IP_SCRAVER/" parameters.json

CMD ["/entry.sh"]
