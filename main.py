from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Origin"]
)

handler = Mangum(app)