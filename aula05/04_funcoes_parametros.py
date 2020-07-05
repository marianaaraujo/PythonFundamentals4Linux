#!/usr/bin/python3

carrinho = []

produto1 = {'nome':'Tenis','valor':21.70}
produto2 = {'nome':'Meia','valor':10}
produto3 = {'nome':'Camiseta','valor':17.30}
produto4 = {'nome':'Calca','valor':100.70}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

def totalCarrinho(carrinho):
    return sum(produto['valor'] for produto in carrinho)

def cupomDesconto(cupom=''):
    if cupom == 'xyzgratis':
        return 1
    else:
        return 0.5

cupom = input('Informe o cupom de desconto: ')

total = totalCarrinho(carrinho)

print('O total da sua compra é: ', total)
print('Com desconto: ', (total * (1 - cupomDesconto())))
print('Utilizando o cupom xyzgratis, o valor será de ', (total * (1 - cupomDesconto(cupom))))