from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..ocorrencia.model import Ocorrencia
    from ..cargo.model import Cargo
    from ..reposicao.model import Reposicao

class Funcionario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_funcionario: str
    login: str
    status: bool
    senha: str
    cod_cargo: int = Field(foreign_key="cargo.id")

    registros: List["Ocorrencia"] = Relationship(back_populates="autor")
    posicao: "Cargo" = Relationship(back_populates="funcionarios")
    repos: "Reposicao" = Relationship(back_populates="repositor")

