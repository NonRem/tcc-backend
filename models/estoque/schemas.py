from sqlmodel import SQLModel
from typing import Optional
from typing import Optional, TYPE_CHECKING
from ..produto.schemas import ProdutoRead

class EstoqueCreate(SQLModel):
    cod_produto: int
    quant_max: int
    quant_min: int
    quant_atual: int

class EstoqueRead(SQLModel):
    quant_max: int
    quant_min: int
    quant_atual: int
    id: int
    mercadoria: "ProdutoRead"

class EstoqueUpdate(SQLModel):
    quant_max: Optional[int]
    quant_min: Optional[int]
    quant_atual: Optional[int]