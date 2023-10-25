from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..produto.model import Produto
    from ..funcionario.model import Funcionario

class Reposicao(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    data: datetime = Field(default=datetime.now())
    quantidade: int

    cod_produto: int = Field(foreign_key="produto.cod_produto")
    id_funcionario: int = Field(foreign_key="funcionario.id")

    repositor: "Funcionario" = Relationship(back_populates="repos")
    item: "Produto" = Relationship(back_populates="recolocado")
