from flask import Flask, request
import pymongo, json
from bson import json_util

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://ROOT_USERNAME:ROOT_PASSWORD@IP_MONGODB:27017/admin')
cursor = client['etl']

@app.route("/test")
def teste():
    return "It Works!", 200

@app.route("/v1/<string:code>")
def lastData(code):
    code = code.upper()
    try:
        lastCode = list(cursor['stocks'].find({"code":code}).sort('date', -1).limit(1))[0]
        lastCode = json.loads(json_util.dumps(lastCode))
        return lastCode, 200
    except:
        return "This code does not exist."


@app.route("/v1/<string:code>/all")
def allLastData(code):
    code = code.upper()
    try:
        lastCode = list(cursor['stocks'].find({"code":code}).sort('date', -1))
        lastCode = json.loads(json_util.dumps(lastCode))
        return lastCode, 200
    except:
        return "This code does not exist.", 404


@app.route("/v1/logs")
def allLogs():
    try:
        allLogs = list(cursor['log'].find().sort('date', -1))
        allLogs = json.loads(json_util.dumps(allLogs))
        return allLogs, 200
    except:
        return "unknown error", 499

@app.route("/v1/logs/<string:code>")
def logs(code):
    code = code.upper()
    try:
        allLogs = list(cursor['log'].find({"code":code}).sort('date', -1))
        allLogs = json.loads(json_util.dumps(allLogs))
        return allLogs, 200
    except:
        return "This code does not exist.", 404
    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
