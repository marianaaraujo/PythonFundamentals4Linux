#!/usr/bin/python3

from sqlalchemy import update
from core import user_table, engine

con = engine.connect()
atualizar = update(user_table).where(user_table.c.nome == 'João Prata')

commit = atualizar.values(nome='João das Neves')
result = con.execute(commit)
print(result.rowcount)