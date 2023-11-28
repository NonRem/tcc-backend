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
from models.alerta.model import Alerta
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")
POSTGRESQL_URL_LOCAL = os.getenv("POSTGRESQL_URL_LOCAL")

engine = create_engine(POSTGRESQL_URL_LOCAL, echo=False)


def create_database_with_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_database_with_tables()
    """ loop = asyncio.get_event_loop()
    loop.add_reader(conn, handle_notify)
    loop.run_forever() """


if __name__ == '__main__':
    main()