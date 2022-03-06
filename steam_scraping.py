import numpy as np
import pandas as pd
import csv
import json
import time
import requests

#Function returns each request that we scrap from the Steam API
def get_requests(url, parameters=None):
    response = requests.get(url=url,params=parameters)

    if response:
        return response.json()


games_ids=pd.read_csv('spyData_nameID_only_sorted.csv')

error_requests=[]
steam_columns = [
        'name', 'steam_appid',  
        'genres',
        'release_date'
    ]

with open("steam_DB_raw.csv",'a',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=steam_columns,extrasaction='ignore')
    writer.writeheader()

for i in range(0,4320):
    xx=[]
    for index,row in games_ids[10*i:10*(i+1)].iterrows():
        print('Index: ',index)
        appid=row['appid']
        name = row['name']

        url="http://store.steampowered.com/api/appdetails/"
        paramss = {"appids":appid}
        try:
            json_data=get_requests(url,parameters=paramss)
            json_app_data = json_data[str(appid)]
            data = json_app_data['data']
            xx.append(data)
        except:
            error_requests.append(index)
        time.sleep(1.6)

    steam_columns = [
        'name', 'steam_appid',  
        'genres',
        'release_date'
    ]
    try:
        with open("steam_DB_raw.csv",'a',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=steam_columns,extrasaction='ignore')
            #writer.writeheader()
            writer.writerows(xx)
    except:
            error_requests.append(index)

    print("errors: "+str(len(error_requests)))
    
    errorTextFile = open("error_list.txt","w")
    for index in error_requests:
        errorTextFile.write(str(index)+"\n")
    errorTextFile.close()