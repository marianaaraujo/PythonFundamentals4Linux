#!/usr/bin/python3

# Documentação do ORM
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

from classes.Entidades import Paciente
from classes.Entidades import Funcionario
from datetime import date
from config.banco import session

paciente = Paciente(
    nome='Joaquim dos Santos',
    dtnasc=date(1982,5,13)
)

recepcionista = Funcionario(
    nome='Marcelo Dantas',
    cargo='Recepcionista',
    dtnasc=date(1978,3,5)
)

medico = Funcionario(
    nome='Marielle Danjou',
    cargo='Médico',
    dtnasc=date(1978,3,5)
)

session.add_all([
    paciente,
    recepcionista,
    medico
])


# session.add(paciente)

session.commit()
# session.rollback()

# query = session.query(Paciente)

# pacientes = query.all()

# for paciente in pacientes:
#     print(
#         paciente.id,
#         paciente.nome,
#         paciente.dtnasc
#     )

# for paciente in session.query(Paciente).filter(
#     Paciente.nome.like('Joaquim%')
# ):
#     print(
#         paciente.id,
#         paciente.nome,
#         paciente.dtnasc
#     )

# paciente = session.query(Paciente).filter(
#     Paciente.nome.like('Joaquim%')
# ).first()

# print(
#     paciente.id,
#     paciente.nome,
#     paciente.dtnasc
# )

# paciente.nome = 'Joaquim da Silva'
# paciente.dtnasc = '1989-05-13'

# session.commit()

# paciente = session.query(Paciente).filter(
#     Paciente.nome.like('Joaquim%')
# ).first()

# print(paciente.id, paciente.nome, paciente.dtnasc)

# session.delete(paciente)
# session.commit()

# print(
#     session.query(Paciente).filter(
#         Paciente.nome.like('Joaquim%')
#     ).count()
# )
