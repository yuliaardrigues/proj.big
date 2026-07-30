from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import SessionLocal, engine, Base
from database.models import Noticia

app = FastAPI(
    title="News Collector API",
    description="API de notícias coletadas automaticamente",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "API de notícias funcionando"
    }

@app.get("/noticias")
def listar_noticias():
    session = SessionLocal()
    noticias = session.query(Noticia).all()
    resultado = []

    for noticia in noticias:
        resultado.append({
            "id": noticia.id,
            "titulo": noticia.titulo,
            "autor": noticia.autor,
            "data": noticia.data,
            "categoria": noticia.categoria,
            "link": noticia.link,
            "data_coleta": noticia.data_coleta
        })

    session.close()
    return resultado