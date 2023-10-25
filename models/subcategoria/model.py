from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..produto.model import Produto

class Subcategoria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo_produto: str

    artigos: List["Produto"] = Relationship(back_populates="subcategoria")

