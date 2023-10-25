from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from models.estoque.model import Estoque
from models.estoque.schemas import EstoqueCreate, EstoqueRead, EstoqueUpdate
from dependencies import get_session
from routes.auth import get_current_user

router = APIRouter(prefix="/estoque", dependencies=[Depends(get_current_user)], tags=["estoque"])

@router.get('/', response_model=List[EstoqueRead])
def get_estoque_todo(session: Session = Depends(get_session)):
    statement = select(Estoque)
    estoque = session.exec(statement).all()
    return estoque

@router.get('/{cod_produto}', response_model=EstoqueRead)
async def get_estoque_item(cod_produto: int, session: Session = Depends(get_session)):
    statement = select(Estoque).where(Estoque.cod_produto == cod_produto)
    estoque = session.exec(statement).first()
    return estoque

@router.post('/add', response_model=EstoqueRead)
def post_estoque(estoque: EstoqueCreate, session: Session = Depends(get_session)):
    estoque_db = Estoque.from_orm(estoque)
    session.add(estoque_db)
    session.commit()
    session.refresh(estoque_db)
    return estoque_db

