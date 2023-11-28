from sqlmodel import SQLModel
from datetime import date
from typing import TYPE_CHECKING
from models.produto.schemas import ProdutoRead
from models.fornecedor.schemas import FornecedorRead

class LoteCreate(SQLModel):
    vencimento: date
    cod_lote: str
    recebimento: date
    cod_produto: int
    id_fornecedor: int
    quantidade: int

class LoteRead(SQLModel):
    vencimento: date
    cod_lote: str
    recebimento: date
    id: int
    quantidade: int
    mercadoria: "ProdutoRead"

class LoteReadShort(SQLModel):
    vencimento: date
    cod_lote: str
    recebimento: date