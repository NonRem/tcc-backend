from sqlmodel import SQLModel
from typing import Optional, TYPE_CHECKING
from ..produto.schemas import ProdutoRead

class MostruarioCreate(SQLModel):
    cod_produto: int
    quant_max: int
    quant_min: int
    quant_atual: int
    quant_perdida: int

class MostruarioRead(MostruarioCreate):
    id: int
    produto: "ProdutoRead"

class MostruarioUpdate(MostruarioRead):
    quant_max: Optional[int]
    quant_min: Optional[int]
    quant_atual: Optional[int]
    quant_perdida: Optional[int]