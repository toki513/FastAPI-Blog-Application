from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase


DATABASE_URL = "postgresql://postgres:123456@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    with SessionLocal() as db:
        yield db