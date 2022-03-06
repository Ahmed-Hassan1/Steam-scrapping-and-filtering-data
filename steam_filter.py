import numpy as np
import pandas as pd
import csv
import json
import time
import requests
import ast


df=pd.read_csv("steam_DB_raw.csv")

print(df.shape)

df= df[ df['genres'].isna() == False ]
df= df[ df['release_date'].isna() == False ]

print(df.shape)

#Filters the columns from JSON objects into a list of strings that contain the genres only
df['genres'] = [list(set([y['description'] for y in x])) for x in df['genres'].apply(ast.literal_eval)]

#Counts the frequency of genres in the column of lists
a = pd.Series([y for x in df['genres'] for y in x]).value_counts()
print(a)



#Fileters the columns from JSON to only contain the release date
# df['release_date'] =df['release_date'].apply(ast.literal_eval)

# err=[]
# for index,row in df.iterrows():
#     try:
#         df['release_date'][index]=df['release_date'][index]['date']
#     except:
#         print(df['release_date'][index])
#         err.append(index)
# print(err)

# err=[]
# for index,row in df.iterrows():
#     try:
#         df['release_date'][index]=pd.to_datetime(df['release_date'][index])
#     except:
#         print(df['release_date'][index])
#         df.drop(index,inplace=True)
#         err.append(index)
# print(df.shape)
# print(err)
# df_sorted=df.sort_values(by='release_date')

# df.to_csv("steam_filtered.csv",index=False)