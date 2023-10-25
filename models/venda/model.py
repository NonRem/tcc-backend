from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional
from datetime import datetime

class Venda(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    valor: float
    produtos: dict = Field(default={}, sa_column=Column(JSON))
    data: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True

