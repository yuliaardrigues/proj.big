import feedparser
from datetime import datetime


class RSSCollector:

    RSS_URLS = [

        "https://slashdot.org/index.rss",
        "https://www.bleepingcomputer.com/feed/",
        "https://tecnoblog.net/feed/",
        "https://www.theregister.com/headlines.atom",
        "https://techcrunch.com/feed/",
        "https://cybersecuritynews.com/feed/",
        "https://www.cnbc.com/id/100003114/device/rss/rss.html",
        "https://www.theverge.com/rss/index.xml",
        "https://feeds.bbci.co.uk/news/technology/rss.xml",
        "https://nerds.xyz/feed/"

    ]


    def parse_article(self, item, fonte):

        return {

            "titulo": item.get(
                "title",
                "Sem título"
            ),

            "autor": item.get(
                "author",
                "Não informado"
            ),

            "data": self.get_date(item),

            "categoria": self.get_category(item),

            "conteudo": item.get(
                "summary",
                ""
            ),

            "link": item.get(
                "link",
                ""
            ),

            "fonte": fonte
        }


    def get_date(self, item):

        # RSS com published_parsed
        if "published_parsed" in item:

            data = item.published_parsed

            return datetime(
                data.tm_year,
                data.tm_mon,
                data.tm_mday,
                data.tm_hour,
                data.tm_min
            )


        # RSS com updated_parsed
        if "updated_parsed" in item:

            data = item.updated_parsed

            return datetime(
                data.tm_year,
                data.tm_mon,
                data.tm_mday,
                data.tm_hour,
                data.tm_min
            )


        # caso venha datetime pronto
        if "published" in item:

            valor = item.published

            if isinstance(valor, datetime):
                return valor


        # caso não tenha data
        return datetime.now()



    def get_category(self, item):

        tags = item.get(
            "tags",
            []
        )

        if tags:

            return tags[0].get(
                "term",
                "Não informada"
            )

        return "Não informada"



    def scrape(self):

        noticias = []


        for url in self.RSS_URLS:

            print(
                f"\n📰 Coletando: {url}"
            )

            try:

                feed = feedparser.parse(url)


                print(
                    f"Encontradas {len(feed.entries)} notícias"
                )


                fonte = url.split("/")[2]


                for item in feed.entries:

                    try:

                        noticia = self.parse_article(
                            item,
                            fonte
                        )


                        noticias.append(
                            noticia
                        )


                    except Exception as erro:

                        print(
                            f"Erro na notícia: {erro}"
                        )


            except Exception as erro:

                print(
                    f"Erro no RSS: {erro}"
                )


        print(
            f"\nTotal coletado: {len(noticias)} notícias"
        )


        return noticias