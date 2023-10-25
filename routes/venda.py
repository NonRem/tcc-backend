from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from dependencies import get_session
from routes.auth import get_current_user
from models.venda import model, schemas
from models.estoque.model import Estoque
from models.mostruario.model import Mostruario
from typing import List
from database import engine

router = APIRouter(prefix='/venda', dependencies=[Depends(get_current_user)], tags=["venda"])

@router.get('/', response_model=List[schemas.VendaRead])
def get_vendas(session: Session = Depends(get_session)):
    statement = select(model.Venda)
    vendas = session.exec(statement).all()
    return vendas

@router.post('/add', response_model=schemas.VendaRead)
def add_venda(venda: schemas.VendaCreate, session: Session = Depends(get_session)):
    venda_db = model.Venda.from_orm(venda)
    session.add(venda_db)
    atualizar_estoque(venda_db.produtos)
    atualizar_mostruario(venda_db.produtos)
    session.commit()
    session.refresh(venda_db)
    
    return venda_db

def atualizar_mostruario(venda: dict):
    with Session(engine) as session:
        for key, value in venda.items():
            statement = select(Mostruario).where(Mostruario.cod_produto == key)
            item_mostruario = session.exec(statement).one()
            item_mostruario.quant_atual -= value["quantidade"]
            session.add(item_mostruario)
            session.commit()

def atualizar_estoque(venda: dict):
    with Session(engine) as session:
        for key, value in venda.items():
            statement = select(Estoque).where(Estoque.cod_produto == key)
            item_estoque = session.exec(statement).one()
            item_estoque.quant_atual -= value["quantidade"]
            session.add(item_estoque)
            session.commit()