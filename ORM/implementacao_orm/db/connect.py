from sqlalchemy import create_engine

def connect():
    db_url = 'postgresql://usuario:senha@localhost:5432/northwind?client_encoding=UTF8'
    engine = create_engine(db_url)
    return engine
