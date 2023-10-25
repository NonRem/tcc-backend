from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt, JWTError
from models.funcionario.model import Funcionario
from database import engine
from sqlmodel import Session, select
from datetime import timedelta, datetime

SECRET_KEY = "teste"
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=20)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
def get_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    usuario = authenticate_user(form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    token = create_access_token(usuario.login, usuario.id)
    jwt_encoded = {"access_token": token, "token_type": "bearer"}

    return jwt_encoded

def create_access_token(login: str, id: int):
    encode = {"login": login, "id": id}
    expiration = datetime.utcnow() + EXPIRATION_TIME
    encode.update({"exp": expiration})
    encoded_token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_token

def authenticate_user(login: str, senha: str):
    with Session(engine) as session:
        usuario = session.exec(select(Funcionario).where(Funcionario.login == login)).first()
        if not usuario:
            return False
        if not usuario.status:
            return False
        if not (usuario.senha == senha):
            return False
    return usuario

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int = payload.get('id')
        login: str = payload.get('login')
        if id is None:
            raise HTTPException(status_code=401, detail="Usuário não pode ser validado.")
    except JWTError:
        raise HTTPException(status_code=401, detail="Usuário não é válido.")
    return {"id": id, "login": login}