#!/usr/bin/python3

class Dog():
    '''Tentando abstrair um cachorro!'''
    dono = None

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 10
        self.sede = 10
        self.fome = 10

    def __del__(self):
        print('Método destrutor executado!')

    def latir(self):
        print('Latindo...')
    
    def andar(self):
        print('Andando...')

    def dormir(self):
        print('ZZZzzzZZZzzz...')

    def beber(self):
        print('Bebendo...')
    
    def comer(self):
        print('Comendo...')

dog1 = Dog('Bilu', 'Pitbull', 2)

#A Classe
print(type(dog1))

print('--------------------------------------------')

#Os métodos
print(dir(dog1))

print('--------------------------------------------')

#A documentação
print(dog1.__doc__)

print('--------------------------------------------')

print(dog1.dono)

dog1.dono = 'Mariana'

print(dog1.dono)

print('--------------------------------------------')

print(dog1.nome, dog1.raca, dog1.idade, sep='\n')

print('--------------------------------------------')

dog1.andar()

print(dog1.nome, '''Energia {} Fome {} Sede {}'''.format(dog1.energia, dog1.fome, dog1.sede))