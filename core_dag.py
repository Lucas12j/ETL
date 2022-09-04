import requests
import pymongo
import time
import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

scraverIp = '[CHANGE TO IP SCRAVER]' #'172.19.0.8'
mongoStringConnection = '[CHANGE TO MONGO DB STRING]' #'mongodb://etl:engenheirodedados@172.19.0.9:27017/admin'

extractionDate = datetime.datetime.today().isoformat()[:10]
data = []
logs_list = []
document_list = []
                                           
def func_extract():  

        post = {
                    "url":"https://www.fundamentus.com.br/detalhes.php?papel=",
                    "dynamic":0,
                    "cssSelector":"body > div.center > div.conteudo.clearfix > div > div",
                    "regex":">(\\w\\w\\w\\w\\d|\\w\\w\\w\\w\\d\\d)<"
            }

        stocksCode = requests.post(url='http://'+scraverIp, json=post).json()['value']


        post = {
                                "dynamic":0,
                                "batch":[
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {

                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(4) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(5) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(6) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(6) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(7) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(7) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(8) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(8) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                             {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(9) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(9) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                             {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(10) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(10) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                             {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(11) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(11) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            },
                                             {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(12) > td:nth-child(4) > span",
                                                "regex":">(.+)<"
                                            },
                                            {
                                                "cssSelector":"body > div.center > div.conteudo.clearfix > table:nth-child(4) > tbody > tr:nth-child(12) > td:nth-child(6) > span",
                                                "regex":">(.+)<"
                                            }
                                        ]


                            }

        for code in stocksCode:
            log = {}
            file = open('realTime.temp', 'a')
            post.update({"url":"https://www.fundamentus.com.br/detalhes.php?papel="+code})

            time1 = time.time()
            try:
                response = requests.post(url='http://'+scraverIp, json=post).json()['values']
                response.append(code)
                data.append(tuple(response))

                log.update(
                {
                    "status":"Collected",
                    "code": code,
                    "date": extractionDate,
                }
                    )

                file.write(code+" ----------- COLETADA.\n")

            except:
                file.write(code+" ----------- NÃO COLETADA.\n")
                log.update(
                {
                    "status":"Not Collected",
                    "code": code,
                    "date": extractionDate,
                }
                    )

            time2 = time.time()
            log.update({"duration":str(time2-time1)})
            logs_list.append(log)
            file.close()

        import os
        os.system("rm realTime.temp")





def func_transform():

        for i in data:
            values = tuple(map(lambda x:x.replace(",","."), i))
            document = {           
                                        "date" : extractionDate,
                                        "code":i[-1],
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

            document_list.append(document)   



def func_load():
        client = pymongo.MongoClient(mongoStringConnection)
        stocksClient = client['etl']['stocks']
        stocksClient.insert_many(document_list)

        logClient = client['etl']['log']
        logClient.insert_many(logs_list)


with DAG('core', start_date = datetime.datetime(2021,9,4), schedule_interval = '0 23 * * *', catchup = False ) as dag:

        func_extract = PythonOperator(
                    task_id = 'func_extract',
                    python_callable = func_extract
            )

        func_transform = PythonOperator(
                    task_id = 'func_transform',
                    python_callable = func_transform
            )

        func_load = PythonOperator(
                    task_id = 'func_load',
                    python_callable = func_load
            )

        func_extract >> func_transform >> func_load
