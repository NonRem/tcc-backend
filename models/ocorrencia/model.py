from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..funcionario.model import Funcionario

class Ocorrencia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_funcionario: int = Field(foreign_key="funcionario.id")
    data: datetime = Field(default=datetime.now(), index=True)
    relatorio: dict = Field(default={}, sa_column=Column(JSON))

    autor: "Funcionario" = Relationship(back_populates="registros")

    class Config:
        arbitrary_types_allowed = True
