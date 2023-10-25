from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from models.mostruario.model import Mostruario
from models.mostruario.schemas import MostruarioRead
from dependencies import get_session
from routes.auth import get_current_user

router = APIRouter(prefix="/mostruario", dependencies=[Depends(get_current_user)], tags=["mostruario"])

@router.get('/', response_model=List[MostruarioRead])
def get_mostruario_todo(session: Session = Depends(get_session)):
    statement = select(Mostruario)
    mostruario = session.exec(statement).all()
    return mostruario  

@router.get('/{cod_produto}', response_model=MostruarioRead)
def get_mostruario_item(cod_produto: int, session: Session = Depends(get_session)):
    statement = select(Mostruario).where(Mostruario.cod_produto == cod_produto)
    mostruario = session.exec(statement).first()
    return mostruario