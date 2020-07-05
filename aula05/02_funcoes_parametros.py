#!/usr/bin/python3

def boas_vindas(nome):
    return 'Seja bem vindo {}!'.format(nome)

print(boas_vindas('Mariana'))

nome = input('Informe seu nome: ')
print(boas_vindas(nome))

#print(boas_vindas())