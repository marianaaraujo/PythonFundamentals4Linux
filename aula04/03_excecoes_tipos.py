#!/usr/bin/python3

produtos = [
    {'nome': 'produto1', 'valor': 2.0},
    {'nome': 'produto2', 'valor': 1.0},
    {'nome': 'produto3', 'valor': 2.5},
    {'nome': 'produto4', 'valor': 3.0}
    #{'nome': 'produto4', 'valor': '3.0'}
]

try:
    for produto in produtos:
        #print(type(produto['valor']))
        #print(produto['valor'])
        produto['valor'] += produto['valor'] * 0.1
        #produto['preco'] += produto['valor'] * 0.1
except KeyError as e:
    print('Chave não encontrada: {}'.format(e))
except Exception as e:
    print('Erro: {}'.format(e))
finally:
    for produto in produtos:
        print(produto['nome'], produto['valor'], sep=' - ')