# main.py
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import FilmeDB
from schemas import FilmeCreate, FilmeResponse
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)



@app.get("/filmes", response_model=list[FilmeResponse])
def listar_filmes(db: Session = Depends(get_db)):
    return db.query(FilmeDB).all()

@app.post("/filmes", response_model=FilmeResponse, status_code=201)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    novo_filme = FilmeDB(**filme.dict())
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

@app.get('/filmes/{filme_id}', response_model=FilmeResponse)
def obter_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(FilmeDB).filter(FilmeDB.id == filme_id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    return filme

@app.put('/filmes/{filme_id}', response_model=FilmeResponse)
def atualizar_filme(filme_id: int, dados: FilmeCreate, db: Session = Depends(get_db)):
    filme = db.query(FilmeDB).filter(FilmeDB.id == filme_id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    
    filme.titulo = dados.titulo
    filme.diretor = dados.diretor
    filme.genero = dados.genero
    filme.ano = dados.ano
    filme.duracao = dados.duracao
    
    db.commit()
    db.refresh(filme)
    return filme

@app.delete('/filmes/{filme_id}')
def remover_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = db.query(FilmeDB).filter(FilmeDB.id == filme_id).first()
    if filme is None:
        raise HTTPException(status_code=404, detail='Filme não encontrado')
    
    db.delete(filme)
    db.commit()
    return {"mensagem": "Filme removido com sucesso"}