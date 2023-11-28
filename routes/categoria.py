from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from dependencies import get_session
from routes.auth import get_current_user
from models.categoria import model, schemas

router = APIRouter(prefix="/categoria", tags=["categoria"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=List[schemas.CategoriaRead])
def get_categoria(session: Session = Depends(get_session)):
    categorias = session.exec(select(model.Categoria)).all()
    return categorias

@router.post("/add", response_model=schemas.CategoriaRead)
def post_categoria(categoria: schemas.CategoriaRead, session: Session = Depends(get_session)):
    categoria_db = model.Categoria.from_orm(categoria)
    session.add(categoria_db)
    session.commit()
    session.refresh(categoria_db)
    return categoria_db