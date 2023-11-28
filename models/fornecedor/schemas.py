from sqlmodel import SQLModel

class FornecedorCreate(SQLModel):
    nome: str
    endereco: str
    telefone: str

class FornecedorRead(FornecedorCreate):
    id: int