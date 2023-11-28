from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from sqlmodel import Session, select
from typing import List
from routes import produto, estoque, lote, mostruario, ocorrencia, reposicao, venda, auth, alerta, categoria, subcategoria, fornecedor
import uvicorn
""" import json
import asyncio
import psycopg2
from dependencies import handle_notify

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class ConnectionManager():
    def __init__(self):
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, token: str):
        await websocket.accept()
        self.active_connections[token] = websocket

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, msg: str):
        for connection in self.active_connections.values():
            await connection.send_text(msg)

manager = ConnectionManager()

messages = []
q = asyncio.Queue()

@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = psycopg2.connect(host='localhost', dbname='db_estoque', user='postgres', password='12345')
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute('LISTEN notificacao;')
    loop = asyncio.get_event_loop()
    loop.add_reader(conn, lambda : messages.append(handle_notify(conn)))
    yield

    conn.close() """

app = FastAPI()

@app.get("/")
def hello():
  return {"Hello": "World"}
""" 
@app.websocket('/ws/{token}')
async def websocket_endpoint(websocket: WebSocket, token: str):
    await manager.connect(websocket, token)

    try:
        while True:
            await q.put(messages[-1])
            await manager.broadcast(q.get())
    except WebSocketException:
        manager.disconnect(websocket)
        message = {"message": "Desconectado"}
        print(message) """

app.include_router(produto.router)
app.include_router(estoque.router)
app.include_router(lote.router)
app.include_router(mostruario.router)
app.include_router(ocorrencia.router)
app.include_router(reposicao.router)
app.include_router(venda.router)
app.include_router(auth.router)
app.include_router(alerta.router)
app.include_router(categoria.router)
app.include_router(subcategoria.router)
app.include_router(fornecedor.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

handler = Mangum(app)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)