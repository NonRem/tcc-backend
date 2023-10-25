from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..funcionario.model import Funcionario

class Cargo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_cargo: str

    funcionarios: List["Funcionario"] = Relationship(back_populates="posicao")
