from sqlmodel import SQLModel
from datetime import date
from typing import TYPE_CHECKING
from ..funcionario.schemas import FuncionarioRead
from pydantic import Extra

class OcorrenciaCreate(SQLModel, extra=Extra.allow):
    relatorio: dict

class OcorrenciaRead(OcorrenciaCreate):
    id: int
    autor: "FuncionarioRead"
    data: date