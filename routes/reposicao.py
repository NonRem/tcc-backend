from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from dependencies import get_session
from routes.auth import get_current_user
from models.reposicao.model import Reposicao
from models.reposicao.schemas import ReposicaoRead, ReposicaoCreate
from models.mostruario.model import Mostruario
from typing import List
from database import engine

router = APIRouter(prefix='/reposicao', dependencies=[], tags=["reposicao"])

@router.post('/add', response_model=ReposicaoRead)
def post_reposicao(reposicao: ReposicaoCreate, session: Session = Depends(get_session), user: dict = Depends(get_current_user)):
    setattr(reposicao, "id_funcionario", user.get("id"))
    reposicao_db = Reposicao.from_orm(reposicao)
    reestocar(reposicao_db)
    session.add(reposicao_db)
    session.commit()
    session.refresh(reposicao_db)
    return reposicao_db

@router.get('/', response_model=List[ReposicaoRead])
def get_reposicoes(session: Session = Depends(get_session), user = Depends(get_current_user)):
    reposicoes = session.exec(select(Reposicao).order_by(Reposicao.data.desc())).all()
    return reposicoes

def reestocar(reposicao: Reposicao):
    with Session(engine) as session:
        statement = select(Mostruario).where(Mostruario.cod_produto == reposicao.cod_produto)
        produto = session.exec(statement).first()
        produto.quant_atual += reposicao.quantidade
        if produto.quant_atual > produto.quant_max:
            produto.quant_perdida += produto.quant_atual - produto.quant_max
            produto.quant_atual = produto.quant_max
        session.add(produto)
        session.commit()