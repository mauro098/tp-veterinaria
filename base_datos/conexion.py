import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

RUTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA_DB = os.path.join(RUTA_BASE, "datos", "veterinaria.db")

engine = create_engine(f"sqlite:///{RUTA_DB}")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass