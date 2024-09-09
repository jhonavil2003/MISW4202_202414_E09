from sqlalchemy import Column, Integer, String, DateTime
from config import Base

class Solicitud(Base):
    __tablename__ = "solicitud"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    fecha_procesamiento = Column(DateTime, nullable=True)