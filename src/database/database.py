from sqlmodel import create_engine, Session, text
from src.core.config import Config

engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True
)

def db_init():
    with engine.begin() as conn:
        conn.execute(text('SELECT 1'))

def get_sessiomn():
    with Session(engine) as session:
        yield session
