from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from dependencies import get_session
from routes.auth import get_current_user
from models.alerta import model, schemas
from typing import List

router = APIRouter(prefix="/alertas", tags=["alertas"], dependencies=[Depends(get_current_user)])

@router.get('/', response_model=List[schemas.AlertaRead])
def get_alertas(session: Session = Depends(get_session)):
    statement = select(model.Alerta).order_by(model.Alerta.data.desc())
    alertas = session.exec(statement).all()
    return alertas

@router.get('/recente', response_model=List[schemas.AlertaRead])
def get_alertas_recentes(session: Session = Depends(get_session)):
    statement = select(model.Alerta).order_by(model.Alerta.data.desc()).limit(5)
    alertas = session.exec(statement).all()
    return alertas