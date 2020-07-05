#!/usr/bin/python3

import csv

#Referência da função open:
#https://docs.python.org/3/library/functions.html#open
with open('arquivo.csv', 'w', newline='') as arq:
    arquivo = csv.writer(arq, delimiter = ';')
    arquivo.writerow(['teste'] * 5)