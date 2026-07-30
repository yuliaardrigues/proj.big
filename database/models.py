from sqlalchemy import Column, Integer, String, Text, DateTime
from database.database import Base


class Noticia(Base):

    __tablename__ = "noticias"


    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )


    titulo = Column(
        String(255),
        nullable=False
    )


    autor = Column(
        String(100)
    )


    data = Column(
        DateTime
    )


    categoria = Column(
        String(100)
    )


    conteudo = Column(
        Text
    )


    link = Column(
        String(500),
        unique=True
    )


    data_coleta = Column(
        DateTime
    )