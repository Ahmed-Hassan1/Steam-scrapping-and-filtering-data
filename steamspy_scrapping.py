import numpy as np
import pandas as pd
import requests
import csv
import json
import time


#Function that returns each request
def get_requests(url, parameters=None):
    response = requests.get(url=url,params=parameters)

    if response:
        return response.json()

#SteamSpy scraping code
url = "https://steamspy.com/api.php"
steam_spy_data=[]
for i in range(0,70):
    params = {"request":"all","page":i}
    json_data = get_requests(url,parameters=params)
    if(json_data):
        steam_spy_data.append(pd.DataFrame.from_dict(json_data,orient='index'))
    time.sleep(61)

pd.concat(steam_spy_data).to_csv('seamSpy_raw_data.csv',index=False)





#here we are starting to filter the data to get relevant results only
df=pd.read_csv("teamSpy_raw_data.csv")
print(df.shape)

#remove any games that are free to play
df_no_free_games=df[ df[ 'initialprice' ] != 0]
print(df_no_free_games.shape)

#Sort the data to get only the relevant data needed to scrap from steam
df_name_id_only = df_no_free_games[['appid','name']]
print(df_name_id_only.head())

df_name_id_only=df_name_id_only.sort_values("appid")

#df_no_free_games.to_csv("spyData_noFreeGames.csv")
#df_name_id_only.to_csv("spyData_nameID_only.csv")
df_name_id_only.to_csv("spyData_nameID_only_sorted.csv",index=False)