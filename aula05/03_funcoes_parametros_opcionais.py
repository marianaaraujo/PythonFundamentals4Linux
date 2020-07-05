#!/usr/bin/python3

def boas_vindas(nome=''):
    if nome != '':
        return 'Seja bem vindo {}!'.format(nome)

print(boas_vindas())
print(boas_vindas('Mariana'))