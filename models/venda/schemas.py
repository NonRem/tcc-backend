from sqlmodel import SQLModel
from datetime import datetime

class VendaCreate(SQLModel):
    valor: float
    produtos: dict

class VendaRead(VendaCreate):
    id: int
    data: datetime