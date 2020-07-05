#!/usr/bin/python3

def cadastro(**pessoa):
    #return pessoa
    #return type(pessoa)
    return 'O usuário {} {} foi cadastrado com sucesso!'.format(pessoa['nome'], pessoa['sobrenome'])

print(cadastro(nome='Mariana',sobrenome='Araujo',idade=31))

def cadastro(pessoa):
    #return pessoa
    #return type(pessoa)
    return 'O usuário {} {} foi cadastrado com sucesso!'.format(pessoa['nome'], pessoa['sobrenome'])

pessoa = {'nome':'Mariana', 'sobrenome':'Araujo', 'idade':31}

print(cadastro(pessoa))