#!/usr/bin/python3

cont = 0
while cont < 10:
    print('Execução {}'.format(cont))
    if cont == 5:
        print('Interrompendo o loop com break')
        break

    cont += 1