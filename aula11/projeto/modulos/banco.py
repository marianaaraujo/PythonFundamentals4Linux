#!/usr/bin/python

from pymongo import MongoClient, DESCENDING
import time

try:
    #con = MongoClient('192.168.201.89',27017)
    con = MongoClient()
    db = con['chat']
except Exception as e:
    print('ERRO: {}'.format(e))
    exit()

def cadastrar_mensagem(nome, mensagem):
    data = {
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime(
            '%d-%m-%Y %H:%M:%S' 
        )
    }
    
    db.chat.insert(data)

def busca_mensagem():
    ultimo = None

    mensagens = [menasagem for mensagem in db.chat.find()]

    for mensagem in mensagens:
        ultimo = [mensagem]
        print("[{}] {} : {} \n".format(
            mensagem['hora'], menasagem['nome'], mensagem['mensagem']
        ))

    while True:
        data = [mensagem for mensagem in db.chat.find().limit(1).sort('_id', DESCENDING)]

        if (len(data) > 0 and (data != ultimo)):
            ultimo = data
            print("[{}] {} : {} \n".format(
            data[0]['hora'], data[0]['nome'], data[0]['mensagem']
        ))

        time.sleep(2)