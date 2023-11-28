from fastapi import APIRouter, Depends
from sqlmodel import select, Session
from typing import List
from models.produto import model, schemas, schema_lote
from dependencies import get_session
from routes.auth import get_current_user

router = APIRouter(prefix="/produto", dependencies=[Depends(get_current_user)], tags=["produto"])

@router.get('/', response_model=List[schemas.ProdutoRead])
def get_produtos(session: Session = Depends(get_session)):
    statement = select(model.Produto)
    produtos = session.exec(statement).all()
    return produtos   

@router.get('/lotes', response_model=List[schema_lote.ProdutoComLotes])
def get_produto_lote(session: Session = Depends(get_session)):
    statement = select(model.Produto)
    produto_lote = session.exec(statement).all()
    return produto_lote

@router.get('/{cod_produto}', response_model=schema_lote.ProdutoComLotes)
def get_produto(cod_produto: int, session: Session = Depends(get_session)):
    statement = select(model.Produto).where(model.Produto.cod_produto == cod_produto)
    produto = session.exec(statement).one()
    return produto

@router.get('/short/{cod_produto}', response_model=schemas.ProdutoShort)
def get_produto_short(cod_produto: int, session: Session = Depends(get_session)):
    produto = session.get(model.Produto, cod_produto)
    return produto

@router.get('/shorts/', response_model=List[schemas.ProdutoShort])
def get_produto_short(session: Session = Depends(get_session)):
    produto = session.exec(select(model.Produto)).all()
    return produto

@router.post('/add', response_model=schemas.ProdutoRead)
def post_produto(produto: schemas.ProdutoCreate, session: Session = Depends(get_session)):
    produto_db = model.Produto.from_db(produto)
    session.add(produto_db)
    session.commit()
    session.refresh(produto_db)
    return produto_db