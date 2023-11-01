from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from dependencies import get_session
from routes.auth import get_current_user
from models.ocorrencia.model import Ocorrencia
from models.ocorrencia.schemas import OcorrenciaRead, OcorrenciaCreate
from models.estoque.model import Estoque
from models.mostruario.model import Mostruario
from typing import List
from database import engine

router = APIRouter(prefix='/ocorrencia', dependencies=[Depends(get_current_user)], tags=["ocorrencia"])

@router.post('/add', response_model=OcorrenciaRead)
def post_ocorrencia(ocorrencia: OcorrenciaCreate, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    setattr(ocorrencia, "id_funcionario", user.get("id"))
    ocorrencia_db = Ocorrencia.from_orm(ocorrencia)
    registrar_relatorio(ocorrencia.relatorio)
    session.add(ocorrencia_db)
    session.commit()
    session.refresh(ocorrencia_db)
    return ocorrencia_db

@router.get('/', response_model=List[OcorrenciaRead])
def get_ocorrencias(session: Session = Depends(get_session)):
    ocorrencias = session.exec(select(Ocorrencia)).all()
    return ocorrencias

def registrar_relatorio(relatorio: dict):
    for key, value in relatorio.items():
        total = 0
        for val in value.values():
            total += int(val)
        perdas = total-int(value["Encontrado"])
        zerar_perdidos(key, total)
        if perdas > 0:
            registrar_perdas(key, perdas)

def registrar_perdas(key: str, perdas: int):
    with Session(engine) as session:
        statement = select(Estoque).where(Estoque.cod_produto == int(key))
        estoque = session.exec(statement).one()
        estoque.quant_atual -= perdas
        session.add(estoque)
        session.commit()

def zerar_perdidos(key: str, item_subt: int):
    with Session(engine) as session:
        statement = select(Mostruario).where(Mostruario.cod_produto == int(key))
        mostruario = session.exec(statement).one()
        mostruario.quant_perdida -= item_subt
        session.add(mostruario)
        session.commit()