from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from ..produto.model import Produto

class Categoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    classificacao: str

    itens: List["Produto"] = Relationship(back_populates="categoria")

