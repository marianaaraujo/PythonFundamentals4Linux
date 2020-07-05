#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    db.pessoas.insert({'_id':3,'nome':'Jonas','dtnasc':'2000-02-15'})
except Exception as e:
    print('Erro: {}'.format(e))