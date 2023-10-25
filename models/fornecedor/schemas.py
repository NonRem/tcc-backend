from sqlmodel import SQLModel

class FornecedorRead(SQLModel):
    id: int
    nome: str
    endereco: str
    telefone: str