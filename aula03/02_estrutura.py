#!/usr/bin/python3

idade = int(input('Digite sua idade: '))
habilitacao = input('Você é habilitado? Sim ou não: ')
dirigir = False

if habilitacao.lower().strip() == 'sim':
    habilitacao = True
else:
    instrutor = input('Você está acompanhado de um instrutor? Sim ou não: ')
    if instrutor.lower().strip() == 'sim':
        dirigir = True

if idade >= 18 and habilitacao == True:
    print('Você pode dirigir!')
elif dirigir:
    print('Boa aula!')
else:
    print('Você não pode dirigir!')