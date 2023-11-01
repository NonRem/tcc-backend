from sqlmodel import SQLModel, create_engine
from models.cargo.model import Cargo
from models.categoria.model import Categoria
from models.estoque.model import Estoque
from models.fornecedor.model import Fornecedor
from models.funcionario.model import Funcionario
from models.lote.model import Lote
from models.mostruario.model import Mostruario
from models.ocorrencia.model import Ocorrencia
from models.produto.model import Produto
from models.reposicao.model import Reposicao
from models.subcategoria.model import Subcategoria
from models.venda.model import Venda
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")

engine = create_engine(POSTGRESQL_URL, echo=False)

def create_database_with_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_database_with_tables()

if __name__ == '__main__':
    main()