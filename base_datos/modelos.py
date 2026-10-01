from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from base_datos.conexion import Base

class PacienteDB(Base):
    __tablename__ = "pacientes"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    especie: Mapped[str] = mapped_column(String(50))
    raza: Mapped[str] = mapped_column(String(50))
    edad: Mapped[int] = mapped_column(Integer)
    dueno: Mapped[str] = mapped_column(String(80))

