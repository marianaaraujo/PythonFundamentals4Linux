#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    db.pessoas.update({'_id':3},{'$pull':{'projetos':{'nome':'Bevops'}}})
    db.pessoas.remove({'_id':3})
except Exception as e:
    print('Erro: {}'.format(e))