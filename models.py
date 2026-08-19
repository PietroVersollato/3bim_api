# models.py
from sqlalchemy import Column, Float, Integer, String
from database import Base

class FilmeDB(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    diretor = Column(String(100), nullable=False)
    genero = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    duracao = Column(Integer, nullable=False)  # duração em minutos