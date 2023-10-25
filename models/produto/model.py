from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from ..categoria.model import Categoria
    from ..subcategoria.model import Subcategoria
    from ..lote.model import Lote
    from ..estoque.model import Estoque
    from ..mostruario.model import Mostruario
    from ..reposicao.model import Reposicao

class Produto(SQLModel, table=True):
    cod_produto: int = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    valor: float
    vol: Optional[int]
    peso: Optional[int]
  
    id_categoria: int = Field(foreign_key="categoria.id")
    id_subcategoria: int = Field(foreign_key="subcategoria.id")

    lotes: List["Lote"] = Relationship(back_populates="mercadoria")
    categoria: "Categoria" = Relationship(back_populates="itens")
    subcategoria: "Subcategoria" = Relationship(back_populates="artigos")
    armazenado: "Estoque" = Relationship(back_populates="mercadoria")
    exposto: "Mostruario" = Relationship(back_populates="produto")
    recolocado: List["Reposicao"] = Relationship(back_populates="item")


