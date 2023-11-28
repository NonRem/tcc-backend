from sqlmodel import SQLModel
from datetime import datetime
from models.produto.schemas import ProdutoShort

class AlertaRead(SQLModel):
    id: int
    data: datetime
    mensagem: str
    tipo: str
    artigo: "ProdutoShort"