#!/usr/bin/python3

#JSON - Javascript object notation

import json

pessoas=[{'nome':'Philadelpho','dtnasc':'1937-06-12'},{'nome':'Philomena','dtnasc':'1928-07-15'}]

print('----------------------------------------------')

strJson = json.dumps(pessoas)

print('list[dict]<=>json')
print(type(strJson))
print(strJson)

print('----------------------------------------------')

dicionario = json.loads(strJson)

print('json<=>list[dict]')
print(type(dicionario))
print(dicionario)

print('----------------------------------------------')