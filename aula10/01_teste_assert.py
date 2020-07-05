#!/usr/bin/python3

def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    return x / y

assert 2 == 2, 'Não'
#assert 2 != 2, 'Não'

try:
    #Testar a função somar
    assert somar(2,2) == 4 , 'Obtido: {}, Esperado: 4'.format(somar(2,2))
    assert somar(2,3) == 6 , 'Obtido: {}, Esperado: 6'.format(somar(2,3))
except Exception as e:
    print(e)

try:   
    #Testar a função subtrair
    assert subtrair(2,2) == 0 , 'Obtido: {}, Esperado: 0'.format(subtrair(2,2))
    assert subtrair(5,3) == 1 , 'Obtido: {}, Esperado: 1'.format(subtrair(5,3))
except Exception as e:
    print(e)

try:
    #Testar a função multiplicar
    assert multiplicar(10,2) == 20 , 'Obtido: {}, Esperado: 20'.format(multiplicar(2,2))
    assert multiplicar(1,3) == 4 , 'Obtido: {}, Esperado: 4'.format(multiplicar(5,3))
except Exception as e:
    print(e)

try:
    #Testar a função dividir
    assert dividir(4,2) == 2 , 'Obtido: {}, Esperado: 2'.format(dividir(4,2))
    assert dividir(9,3) == 2 , 'Obtido: {}, Esperado: 2'.format(dividir(9,3))
except Exception as e:
    print(e)