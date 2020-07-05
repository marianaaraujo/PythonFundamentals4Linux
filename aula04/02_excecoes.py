#!/usr/bin/python3

while True:
    num = input('Digite um número: ')

    if num == 'sair':
        break

    #if num.isnumeric():
    #    print(int(num) + 2)
    #else:
    #    print('num não é um número!')

    try:
        print(int(num) + 2)
    except Exception as e:
        print(e)
        print('num não é um número!')


    


