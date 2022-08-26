from flask import Flask, request, jsonify
from scraper import scraperb, scrapers

app = Flask(__name__)

@app.route("/test")
def test():
    return "It Works!", 200

@app.route("/", methods=['POST'])
def scraper():
    data = request.get_json()


    if 'batch' in data.keys():
        cssSelector = [i['cssSelector'] for i in data['batch']]
        regex = [i['regex'] for i in data['batch']]

        if data['dynamic'] == 0:
            scraper = scraperb.ScraperB(url = data['url'], cssSelector = cssSelector, regex = regex)
        elif data['dynamic'] == 1:
            if 'sleepTime' not in data.keys():
                scraper = scrapers.ScraperS(url = data['url'], cssSelector = cssSelector, regex = regex)
            else:
                scraper = scrapers.ScraperS(url = data['url'], cssSelector = cssSelector, regex = regex, sleepTime = data['sleepTime'])

        return {"values":scraper.getValues()[0]}, scraper.getValues()[1]
    else:

        if data['dynamic'] == 0 and 'regex' not in data.keys():
            scraper = scraperb.ScraperB(data['url'], data['cssSelector'])

        elif data['dynamic'] == 0 and 'regex' in data.keys():
            scraper = scraperb.ScraperB(url = data['url'], cssSelector = data['cssSelector'], regex = data['regex'])

        elif data['dynamic'] == 1 and 'sleepTime' not in data.keys() and 'regex' not in data.keys():
            scraper = scrapers.ScraperS(url = data['url'], cssSelector = data['cssSelector'])

        elif data['dynamic'] == 1 and 'sleepTime' not in data.keys() and 'regex' in data.keys():
            scraper = scrapers.ScraperS(url = data['url'], cssSelector = data['cssSelector'], regex = data['regex'])

        elif data['dynamic'] == 1 and 'sleepTime' in data.keys() and 'regex' not in data.keys():
            scraper = scrapers.ScraperS(url = data['url'], cssSelector = data['cssSelector'], sleepTime = data['sleepTime'])

        elif data['dynamic'] == 1 and 'sleepTime' in data.keys() and 'regex' in data.keys():
            scraper = scrapers.ScraperS(url = data['url'], cssSelector = data['cssSelector'], regex = data['regex'], sleepTime = data['sleepTime'])

        return {"value":scraper.getValue()[0]}, scraper.getValue()[1]

app.run(port=80, host='0.0.0.0')