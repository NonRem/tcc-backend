from fastapi import APIRouter, Depends
from dependencies import get_session
from models.lote.auxiliar import adicionar_produtos
from routes.auth import get_current_user
from models.lote.model import Lote
from models.lote.schemas import LoteRead, LoteCreate
from sqlmodel import Session, select
from typing import List

router = APIRouter(prefix="/lote", dependencies=[Depends(get_current_user)], tags=["lote"])

@router.get('/', response_model=List[LoteRead])
def get_lotes(session: Session = Depends(get_session)):
    statement = select(Lote).order_by(Lote.recebimento.desc())
    produto_lote = session.exec(statement).all()
    return produto_lote

@router.get('/{cod_lote}', response_model=List[LoteRead])
def get_lote(cod_lote = int, session: Session = Depends(get_session)):
    statement = select(Lote).where(Lote.cod_lote == cod_lote)
    lote = session.exec(statement).all()
    return lote

@router.post('/add/', response_model=LoteRead)
def add_lote(lote: LoteCreate, session: Session = Depends(get_session)):
    lote_db = Lote.from_orm(lote)
    adicionar_produtos(lote)
    session.add(lote_db)
    session.commit()
    session.refresh(lote_db)
    return lote_db
