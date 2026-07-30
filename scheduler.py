import schedule
import time
from main import coletar_noticias

coletar_noticias()
print("Coletor iniciado...")


while True:

    schedule.run_pending()

    time.sleep(60)