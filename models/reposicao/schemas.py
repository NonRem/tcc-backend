from sqlmodel import SQLModel
from datetime import datetime
from typing import TYPE_CHECKING
from ..produto.schemas import ProdutoRead
from ..funcionario.schemas import FuncionarioRead
from pydantic import Extra

class ReposicaoCreate(SQLModel, extra=Extra.allow):
    quantidade: int
    cod_produto: int

class ReposicaoRead(ReposicaoCreate):
    id: int
    data: datetime
    repositor: "FuncionarioRead"
    item: "ProdutoRead"
