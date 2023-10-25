from fastapi import FastAPI, Depends, Query
from sqlmodel import Session, select
from database import engine
from typing import List
from routes import produto, estoque, lote, mostruario, ocorrencia, reposicao, venda, auth


app = FastAPI()

app.include_router(produto.router)
app.include_router(estoque.router)
app.include_router(lote.router)
app.include_router(mostruario.router)
app.include_router(ocorrencia.router)
app.include_router(reposicao.router)
app.include_router(venda.router)
app.include_router(auth.router)
