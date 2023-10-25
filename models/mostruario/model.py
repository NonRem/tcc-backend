from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..produto.model import Produto

class Mostruario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cod_produto: int = Field(foreign_key="produto.cod_produto" ,unique=True)
    quant_max: int
    quant_min: int
    quant_atual: int
    quant_perdida: int

    produto: "Produto" = Relationship(back_populates="exposto")
