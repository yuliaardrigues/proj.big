from datetime import datetime, timedelta


def is_recent(data_noticia):

    if not data_noticia:
        return False

    if not isinstance(data_noticia, datetime):
        print(f"Data em formato inesperado: {data_noticia!r}")
        return False

    agora = datetime.now()
    limite = agora - timedelta(hours=24)

    return data_noticia >= limite