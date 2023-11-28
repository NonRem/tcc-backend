from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from dependencies import get_session
from routes.auth import get_current_user
from models.fornecedor import model, schemas

router = APIRouter(prefix="/fornecedor", tags=["fornecedor"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=List[schemas.FornecedorRead])
def get_fornecedores(session: Session = Depends(get_session)):
    fornecedores = session.exec(select(model.Fornecedor)).all()
    return fornecedores

@router.post("/add", response_model=schemas.FornecedorCreate)
def post_fornecedor(fornecedor: schemas.FornecedorCreate, session: Session = Depends(get_session)):
    fornecedor_db = model.Fornecedor.from_orm(fornecedor)
    session.add(fornecedor_db)
    session.commit()
    session.refresh(fornecedor_db)
    return fornecedor_db