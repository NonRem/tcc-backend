from sqlmodel import SQLModel
from typing import TYPE_CHECKING
from ..cargo.schemas import CargoRead

class FuncionarioRead(SQLModel):
    id: int
    nome_funcionario: str
    login: str
    status: bool
    posicao: "CargoRead"