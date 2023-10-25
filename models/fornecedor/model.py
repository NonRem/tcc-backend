from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..lote.model import Lote

class Fornecedor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    endereco: str
    telefone: str

    entregas: List["Lote"] = Relationship(back_populates="vendedor")

