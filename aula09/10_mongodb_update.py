#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    db.pessoas.update({'_id':1},{'$set':{'projetos':[]}})
    db.pessoas.update({'_id':3},{'$push':{'projetos':{'nome':'Bevops','desc':'API'}}})
except Exception as e:
    print('Erro: {}'.format(e))