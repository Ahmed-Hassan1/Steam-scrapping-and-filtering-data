import numpy as np
import pandas as pd
import csv
import json
import time
import requests
import ast


steamSpy_raw=pd.read_csv("teamSpy_raw_data.csv")
steam_filtered=pd.read_csv("steam_filtered.csv")

# steam_filtered=steam_filtered[['name','steam_appid','genres','release_date']]
# print(steam_filtered.head())

steam_filtered.rename(columns={'steam_appid':'appid'},inplace = True)

# steamSpy_raw=steamSpy_raw[['appid','name','positive','negative','owners','price','init']]
# print(steamSpy_raw.head())

df=steamSpy_raw.merge(steam_filtered,on='appid')
df=df[['appid','name','positive','negative','owners','price','init','genres','release_date']]
df.head()

df.to_csv('final_data.csv',index=False)