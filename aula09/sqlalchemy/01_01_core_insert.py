#!/usr/bin/python3

from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

#new = ins.values(idade=24, nome='Daniel', senha='teste123')
#con.execute(new)

con.execute(ins,[
    {'nome': 'João', 'idade': 38, 'senha':'senha123'},
    {'nome': 'Maria', 'idade': 25, 'senha':'123@mudar'}
])