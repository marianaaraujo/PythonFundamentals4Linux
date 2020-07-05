#!/usr/bin/python3

import csv

produtos=[{'nome':'Produto A','preco':'125.57'},
          {'nome':'Produto B','preco':'571.25'},
          {'nome':'Produto C','preco':'712.55'}]

#Referência da função open:
#https://docs.python.org/3/library/functions.html#open

with open('produtos.csv', 'w', newline = '') as arq:
    arquivo = csv.writer(arq, delimiter = ';')
    arquivo.writerow(['nome', 'preco'])

    for produto in produtos:
        arquivo.writerow([produto['nome'], produto['preco']])