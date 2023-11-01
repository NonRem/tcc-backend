from sqlmodel import SQLModel
from typing import Optional, List, TYPE_CHECKING
from models.categoria.schemas import CategoriaRead
from models.subcategoria.schemas import SubcategoriaRead

class ProdutoCreate(SQLModel):
    cod_produto: int
    nome: str
    valor: float
    vol: Optional[int]
    peso: Optional[int]
    categoria: int
    subcategoria: int

class ProdutoRead(SQLModel):
    cod_produto: int
    nome: str
    valor: float
    vol: Optional[int]
    peso: Optional[int]
    categoria: "CategoriaRead"
    subcategoria: "SubcategoriaRead"

class ProdutoShort(SQLModel):
    cod_produto: int
    nome: str
    valor: float