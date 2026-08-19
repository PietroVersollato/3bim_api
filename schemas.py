# schemas.py
from pydantic import BaseModel


class FilmeBase(BaseModel):
    titulo: str
    diretor: str
    genero: str
    ano: int
    duracao: int  # duração em minutos

class FilmeCreate(FilmeBase):
    pass

class FilmeResponse(FilmeBase):
    id: int
    
    class Config:
        from_attributes = True