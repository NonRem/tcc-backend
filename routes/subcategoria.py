from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from dependencies import get_session
from routes.auth import get_current_user
from models.subcategoria import model, schemas

router = APIRouter(prefix="/subcategoria", tags=["subcategoria"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=List[schemas.SubcategoriaRead])
def get_subcategoria(session: Session = Depends(get_session)):
    subcategorias = session.exec(select(model.Subcategoria)).all()
    return subcategorias

@router.post("/add", response_model=schemas.SubcategoriaRead)
def post_subcategoria(subcategoria: schemas.SubcategoriaRead, session: Session = Depends(get_session)):
    subcategoria_db = model.Subcategoria.from_orm(subcategoria)
    session.add(subcategoria_db)
    session.commit()
    session.refresh(subcategoria_db)
    return subcategoria_db