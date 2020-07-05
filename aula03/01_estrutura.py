#!/usr/bin/python3

idade = int(input('Digite sua idade: '))
habilitacao = input('Você é habilitado? Sim ou não: ')

if habilitacao.lower().strip() == 'sim':
    habilitacao = True

if idade >= 18 and habilitacao == True:
    print('Você pode dirigir!')
else:
    print('Você não pode dirigir!')