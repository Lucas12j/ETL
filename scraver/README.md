# Scraver

:construction:  Project in Construction  :construction:
<br>
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=Alpha%20Version&color=GREEN&style=for-the-badge)
<br><br>
## Technologies:

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-3776AB?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/Selenium-3776AB?style=for-the-badge&logo=selenium&logoColor=white"/> <img src="https://img.shields.io/badge/Firefox-3776AB?style=for-the-badge&logo=firefox&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-3776AB?style=for-the-badge&logo=flask&logoColor=white"/>
<br><br>
## Description:

Scraver is a dedicated tool for scraping data on the web. Was planned to be a microservice with one function, to receive the collection parameters and returning the clean data. It can be used to collect data on static web pages or web page with dynamic javascript.
<br><br>
## Installation:

1. A Scraver docker image can be mounted using the following command:

```bash
docker build -t lucas12j/scraver .
```
   - You can also download a scraver image ready from Docker Hub from the following command:

```
docker pull lucas12j/scraver:latest
```

2. To generate a scraver container, run the following command:

```
docker run -ti --name scraver --hostname scraver -p 8080:80 lucas12j/scraver
```
<br><br>
## How use:

After installation, the tool will be ready to use. For more information, see the official Scraver documentation, available in following address:
> http://152.67.52.155/docscraver.html

### Hello world

In this first test, a request will be sent to the microservice. In this request we will collect the developer's contact data, available on the main page of the tool's documentation. 

For send the request, we will use the [cUrl](https://curl.se/).

``` cUrl
curl -H "Content-Type: application/json" -X POST -d '{"url":"http://152.67.52.155/docscraver.html", "cssSelector":"#api-_footer > div:nth-child(3) > a", "dynamic":0}' http://localhost:8080
```
Note that the data came dirty with html tags. For to clean, just add the regex parameter, with a regular expression capable of executing the function.

``` cUrl
curl -H "Content-Type: application/json" -X POST -d '{"url":"http://152.67.52.155/docscraver.html", "cssSelector":"#api-_footer > div:nth-child(3) > a", "dynamic":0, "regex":">(.+)<"}' http://localhost:8080
```

### More Info:

1. In the last example, a static site scrape was used. To perform a scrape on a site with dynamic javascript, it is necessary to change the "dynamic" parameter to 1.
2. In a dynamic scrape, you can set a timeout to make sure the data has been collected correctly. Just set this time in the "sleepTime" parameter.
