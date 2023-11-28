from sqlmodel import Session
from database import engine

def get_session():
    with Session(engine) as session:
        yield session

""" def handle_notify(conn):
    conn.poll()
    for notify in conn.notifies:
        notificacao = notify.payload
        print(notify.payload)
    conn.notifies.clear()
    return notificacao """