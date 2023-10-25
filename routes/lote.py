from fastapi import APIRouter, Depends
from dependencies import get_session
from routes.auth import get_current_user
from models.lote.model import Lote
from models.lote.schemas import LoteRead, LoteCreate
from sqlmodel import Session, select
from typing import List

router = APIRouter(prefix="/lote", dependencies=[Depends(get_current_user)], tags=["lote"])

@router.get('/', response_model=List[LoteRead])
def get_lotes(session: Session = Depends(get_session)):
    statement = select(Lote)
    produto_lote = session.exec(statement).all()
    return produto_lote

@router.get('/{cod_lote}', response_model=LoteRead)
def get_lote(cod_lote = int, session: Session = Depends(get_session)):
    statement = select(Lote).where(Lote.cod_lote == cod_lote)
    lote = session.exec(statement).first()
    return lote