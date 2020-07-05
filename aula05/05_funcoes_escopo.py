#!/usr/bin/python3

nome = 'Anonimo'

def boas_vindas():
    #glbobal nome
    nome = 'Mariana'
    return 'Seja bem vindo {}!'.format(nome)

print(boas_vindas())
print(nome)