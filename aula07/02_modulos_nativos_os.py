#!/usr/bin/python3

import os

print('---------------------------------------------------')

#Método getlogin() retorna o usuário logado no sistema operacional
#Não funciona em algumas distriuições linux por não conter variável de ambiente necessária (username)
#Digite env no terminal para verificar variáveis de ambiente
#print('Usuário logado no sistema', os.getlogin(), sep=': ')

#Método getpass.getuser() retorna o usuário logado no sistema operacional

import getpass

print('Usuário logado no sistema', getpass.getuser(), sep=': ')

print('---------------------------------------------------')

#Método listdir(caminhoo='.') retorna um objeto list com a lista de diretórios e arquivos
#no caminho informado, se o parâmetro caminho não for informado retornará o list do
#diretório atual (do script em execução)
print('Listar diretório', os.listdir(), sep=': ')
print('Listar diretório', os.listdir('/home/developer'), sep=': ')

print('---------------------------------------------------')

#Criando diretórios
print('Criar diretório', os.mkdir('pythondir'), sep=': ')
print('Criar diretório', os.mkdir('pythondir2'), sep=': ')

#Gravando um arquivo
with open('pythondir2/testemodulo.txt', 'w') as arquivo:
    arquivo.write('teste')

#Renomeando diretório
print('Renomear diretório', os.rename('pythondir', 'pythonrenomeado'), sep=': ')

#Renomeando arquivo
print('Renomear arquivo', os.rename('pythondir2/testemodulo.txt', 'pythondir2/renomemodulo.txt'), sep=': ')

print('---------------------------------------------------')

#Executando comandos do S.O.
os.system('sudo apt update')

print('---------------------------------------------------')