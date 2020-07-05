#!/usr/bin/python3

class Carro():
    __proprietario = 'Joaquim'

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'gasolina'

    def __del__(self):
        print('Método destrutor executado!')

    def acelerar(self):
        print('Vruuun')

    def freiar(self):
        print('Freiando...')

    def getProprietario(self):
        return self.__proprietario

    def setProprietario(self, proprietario):
        self.__proprietario = proprietario

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'elétrico'

    def acelerar(self):
        print('Shiiifff...')

car1 = Carro('BMW', 'i320', 2016)

print(car1.modelo, car1.combustivel)

car1.acelerar()

print('Proprietário', car1.getProprietario(), sep='\n')
#print('Proprietário', car1.__Proprietario, sep='\n')

print('----------------------------------------------')

car2 = CarroEletrico('Chevrolet', 'Bolt', 2018)

print(car2.modelo, car2.combustivel)
car2.acelerar()

print('Proprietário', car2.getProprietario(), sep='\n')
#print('Proprietário', car2.__Proprietario, sep='\n')

print('----------------------------------------------')

proprietario = input('Informe o proprietário do carro elétrico: ')

car2.setProprietario(proprietario.strip())

print('Proprietário', car2.getProprietario(), sep='\n')