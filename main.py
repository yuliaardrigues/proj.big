from datetime import datetime
from collectors.slashdot import RSSCollector
from utils.date_filter import is_recent
from database.database import engine, Base, SessionLocal
from database.models import Noticia


Base.metadata.create_all(engine)


def coletar_noticias():

    print("\n Iniciando coleta...")
    print("Data da coleta:", datetime.now())


    scraper = RSSCollector()

    noticias = scraper.scrape()

    session = SessionLocal()
    total_salvas = 0

    for noticia in noticias:

        # Filtro de últimas 24 horas
        if not is_recent(noticia["data"]):

            print(
                f"⏳ Notícia antiga ignorada: {noticia['titulo']}"
            )

            continue


        # Verifica duplicidade pelo link
        existe = session.query(Noticia).filter_by(
            link=noticia["link"]
        ).first()

        if existe:

            print(
                f"🔁 Duplicada ignorada: {noticia['titulo']}"
            )

            continue

        # Cria nova notícia
        nova_noticia = Noticia(

            titulo=noticia["titulo"],

            autor=noticia["autor"],

            data=noticia["data"],

            categoria=noticia["categoria"],

            conteudo=noticia["conteudo"],

            link=noticia["link"],

            data_coleta=datetime.now()
        )

        session.add(nova_noticia)

        total_salvas += 1

        print(
            f"✅ Salvando: {noticia['titulo']}"
        )

    session.commit()

    session.close()

    print(
        f"\nFinalizado! {total_salvas} novas notícias salvas."
    )

# Permite executar manualmente
if __name__ == "__main__":

    coletar_noticias()