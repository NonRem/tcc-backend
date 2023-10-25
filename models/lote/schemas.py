from sqlmodel import SQLModel
from datetime import date
from typing import TYPE_CHECKING
from models.produto.schemas import ProdutoRead
from models.fornecedor.schemas import FornecedorRead

class LoteCreate(SQLModel):
    vencimento: date
    cod_lote: int
    recebimento: date
    cod_produto: int
    id_fornecedor: int

class LoteRead(SQLModel):
    vencimento: date
    cod_lote: int
    recebimento: date
    id: int
    mercadoria: "ProdutoRead"
    vendedor: "FornecedorRead"

class LoteReadShort(SQLModel):
    vencimento: date
    cod_lote: int
    recebimento: date