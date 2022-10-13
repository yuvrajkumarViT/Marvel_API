# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from hashlib import md5
import pandas as pd
import requests
import json
import hashlib

def create_df(pub_k,nameStartsWith,hash):
    url="https://gateway.marvel.com:443/v1/public/characters"
    df=[]
    headers={'Content-Type':'application/json'}
    n=0
    for i in range(4):
        param={'apikey' : pub_k,
            'nameStartsWith': 'sa',
            'ts' : '2',
            'hash' : hash, 
            'offset': n,
            'limit' : 100}
        n+=100
        response=requests.get(url,headers=headers,params=param,verify=False)
        #response.raise_for_statusresult=response.json()
        results=response.json()
               
        op=results
        new_row = []
        for a in op['data']['results']:
    
            new_row.append(a['name'])
            new_row.append(a['events']['available'])
            new_row.append(a['series']['available'])
            new_row.append(a['stories']['available'])
            new_row.append(a['comics']['available'])
            new_row.append(a['id'])
            df.append(new_row)
            new_row=[]
    df_main = pd.DataFrame(df,columns=['Character_Name','Events','Series','Stories','Comis','id'])
    return df_main

