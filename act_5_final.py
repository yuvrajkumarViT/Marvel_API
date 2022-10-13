# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:46:37 2022

@author: Yuvraj
"""
from hashlib import md5
import requests
import json
import hashlib
import json
from pandas import DataFrame
import pandas as pd
from package import dataframe_creation
import argparse





    
#pub_k = input("Enter public key")
#pvt_k = input("enter private key")
#nameStartsWith=input("enter private key")
#hash = input("enter hash")



parser=argparse.ArgumentParser(description="enter details")

parser.add_argument('pub_ki',type=str)
parser.add_argument('pvt_ki',type=str)
parser.add_argument('nameStartsWithi',type=str)
parser.add_argument('hashi',type=str)

args=parser.parse_args()
pub_k=args.pub_ki
pvt_k=args.pvt_ki
nameStartsWith=args.nameStartsWithi
hash=args.hashi


df=dataframe_creation.create_df(pub_k,nameStartsWith,hash)

print(df)











