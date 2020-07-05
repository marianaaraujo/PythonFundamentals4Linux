#!/usr/bin/python3

#Referência: https://docs.python.org/3/library.datetime.html

from datetime import datetime
from datetime import date

print('-----------------------------------------------')

print('Data atual', datetime.now(), sep=': ')

print('-----------------------------------------------')

#Tabela completa com simbolos para strftime: 
#https://docs.python.org/2/library/datetime.html#strftime-strftime-behavior

print('Data atual formatada',datetime.now().strftime('%d/%m/%Y %H:%M:%S'), sep=': ')

print('-----------------------------------------------')

hoje = date.today()

#hoje + 45 dias

data_final = date.fromordinal(hoje.toordinal() + 45)
diferenca = data_final - hoje

print('Início {}\nFim {}\nDiferença {} dias'.format(hoje.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y'), diferenca.days))

print('-----------------------------------------------')

data_nascimento = date(1988,3,21)
hoje = date.today()
dias = hoje - data_nascimento
idade = int (dias.days / 365)

print('Idade: {} anos'.format(idade))

print('-----------------------------------------------')