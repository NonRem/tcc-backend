from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from models.mostruario.model import Mostruario
from models.mostruario.schemas import MostruarioRead, MostruarioUpdate, MostruarioCreate
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

@router.post('/add', response_model=MostruarioRead)
def post_mostruario(mostruario: MostruarioCreate, session: Session = Depends(get_session)):
    mostruario_db = Mostruario.from_orm(mostruario)
    session.add(mostruario_db)
    session.commit()
    session.refresh(mostruario_db)
    return mostruario_db

@router.patch('/{cod_produto}', response_model=MostruarioRead)
def patch_mostruario_item(cod_produto: int, new_mostruario: MostruarioUpdate, session: Session = Depends(get_session)):
    statement = select(Mostruario).where(Mostruario.cod_produto == cod_produto)
    mostruario_db = session.exec(statement).first()
    mostruario_dict = new_mostruario.dict(exclude_unset=True)
    for key, value in mostruario_dict.items():
        setattr(mostruario_db, key, value)
    session.add(mostruario_db)
    session.commit()
    session.refresh(mostruario_db)
    return mostruario_db 
