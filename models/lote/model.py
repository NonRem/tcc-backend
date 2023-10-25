from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime, date

if TYPE_CHECKING:
    from ..produto.model import Produto
    from ..fornecedor.model import Fornecedor

class Lote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vencimento: date = Field(index=True)
    cod_lote: int = Field(index=True)
    recebimento: date
    cod_produto: int = Field(foreign_key="produto.cod_produto")
    id_fornecedor: int = Field(foreign_key="fornecedor.id")

    mercadoria: "Produto" = Relationship(back_populates="lotes")
    vendedor: "Fornecedor" = Relationship(back_populates="entregas")

