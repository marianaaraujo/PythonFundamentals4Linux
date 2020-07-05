#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, MetaData, Table,
	                    Column, Integer, String, Date,
                         DateTime, ForeignKey)


engine = create_engine(
    'postgresql://admin:4linux@localhost/projeto', echo=False
)

metadata = MetaData(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

paciente_table = Table('paciente', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('dtnasc', Date)
)

funcionario_table = Table('funcionario', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50)),
    Column('cargo', String(50)),
    Column('dtnasc', Date)
)

consulta_table = Table('consulta', metadata,
    Column('id', Integer, primary_key=True),
    Column(
        'paciente_id',
        None,
        ForeignKey('paciente.id')
    ),
    Column(
        'recepcionista_id',
        None,
        ForeignKey('funcionario.id')
    ),
    Column('medico_id', None, ForeignKey('funcionario.id')),
    Column('data', DateTime)
)

metadata.create_all(engine)