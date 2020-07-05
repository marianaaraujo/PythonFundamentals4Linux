#!/usr/bin/python3

from pymongo import MongoClient
from pprint import pprint

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    #for pessoa in db.pessoas.find():
    #    pprint(pessoa)   
    #pprint([pessoa for pessoa in db.pessoas.find()])
    pprint([pessoa for pessoa in db.pessoas.find({"_id":1})])
except Exception as e:
    print('Erro: {}'.format(e))