from models.lote.schemas import LoteCreate
from models.estoque.model import Estoque
from database import engine
from sqlmodel import Session, select

def adicionar_produtos(lote: LoteCreate):
    with Session(engine) as session:
        estoque_db = session.exec(select(Estoque).where(Estoque.cod_produto == lote.cod_produto)).first()
        estoque_db.quant_atual = estoque_db.quant_atual + lote.quantidade
        session.add(estoque_db)
        session.commit()