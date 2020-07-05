from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, ForeignKey

Base = declarative_base()

class Consulta(Base):
    __tablename__ = 'consulta'

    id = Column(Integer, primary_key=True)
    paciente_id = Column(ForeignKey('paciente.id'))
    paciente = relationship(
        "Paciente", back_populates="consultas"
    )
    recepcionista_id = Column(ForeignKey('funcionario.id'))
    medico_id = Column(ForeignKey('funcionario.id'))
    data = Column(DateTime)


class Funcionario(Base):
    __tablename__ = 'funcionario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cargo = Column(String(50))
    dtnasc = Column(Date)


class Paciente(Base):
    __tablename__ = 'paciente'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    dtnasc = Column(Date)

    consultas = relationship(
        "Consulta", back_populates="paciente"
    )