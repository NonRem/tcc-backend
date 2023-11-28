from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..produto.model import Produto

class Alerta(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    data: datetime = Field(default=datetime.now())
    mensagem: str
    tipo: str

    cod_produto: int = Field(foreign_key="produto.cod_produto")

    artigo: "Produto" = Relationship(back_populates="notificacao")