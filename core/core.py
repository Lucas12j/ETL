##############  BEGIN EXTRACT ###############                                                
import requests
import json

with open('parameters.json', 'r') as file:
    parameters = json.load(file)
urlScraver = parameters['urlScraver']

def codeStocksCollector():
    post = parameters['scraverParameter1']
    r = requests.post(url=urlScraver, json=post).json()
    return r['value']

def dataCollector(stocksCode):    
    post = parameters['scraverParameter2']
    post.update({"url":"https://www.fundamentus.com.br/detalhes.php?papel="+stocksCode})
    r = requests.post(url=urlScraver, json=post).json()
    return r['values']

################  END EXTRACT ##################



##############  BEGIN TRANSFORM ################
import datetime
import time

extractionDate = datetime.datetime.today().isoformat()[:10]

reject_codes = []
document_list = []
logs_list = []


for i in codeStocksCollector():
    file = open('realTime.temp', 'a')
    log = {}
    time1 = time.time()
    try:
        values = list(map(lambda x:x.replace(",","."), dataCollector(i)))
        document = {           
                                    "date" : extractionDate,
                                    "code":i,
                                    "data" : {
                                                "p-l" : values[0],  
                                                "lpa" : values[1],
                                                "p-vp" : values[2],
                                                "vpa" : values[3],
                                                "p-ebit" : values[4],
                                                "marg_bruta" : values[5],
                                                "psr" : values[6],
                                                "marg_ebit" : values[7],
                                                "p-ativos" : values[8],
                                                "marg_liquida" : values[9],
                                                "p-cap_giro" : values[10],
                                                "ebit-ativo" : values[11],
                                                "p-ativ_circ_liq" : values[12],
                                                "roic" : values[13],
                                                "div_yield" : values[14],
                                                "roe" : values[15],
                                                "ev-ebitda" : values[16],
                                                "liquidez_corr" : values[17],
                                                "ev-ebit" : values[18],
                                                "div_br-patrim" : values[19],
                                                "cres_rec_(5a)" : values[20],
                                                "giro_ativos" : values[21]
                                        }    
       }
        log.update(
            {
                "status":"Collected",
                "code": i,
                "date": extractionDate,
            }
                )      
        document_list.append(document)   
        file.write(i+" ----------- COLETADA.\n")             
    except:
        reject_codes.append(i)
        log.update(
            {
                "status":"Not Collected",
                "code": i,
                "date": extractionDate,
            }
                ) 
        file.write(i+" ----------- NÃO COLETADA.\n") 

    time2 = time.time()
    log.update({"duration":str(time2-time1)})
    logs_list.append(log)
    file.close()

import os
os.system("rm realTime.temp")
##############  END TRANSFORM ################



################  BEGIN LOAD ###################
import pymongo

client = pymongo.MongoClient(parameters['mongoStringConnect'])
stocksClient = client['etl']['stocks']
stocksClient.insert_many(document_list)

logClient = client['etl']['log']
logClient.insert_many(logs_list)
################  END LOAD ###################
