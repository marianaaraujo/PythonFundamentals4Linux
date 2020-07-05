#!/usr/bin/python3

from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, Date)

engine = create_engine('postgresql://admin:4linux@localhost/projeto', echo=False)
metadata = MetaData(bind=engine)

user_table = Table(
    'usuarios', 
    metadata, 
    Column('id', Integer, primary_key=True), 
    Column('nome', String(50)),
    Column('dtnasc', Date  )
    )

metadata.create_all(engine)