from sqlmodel import SQLModel

class CargoRead(SQLModel):
    nome_cargo: str