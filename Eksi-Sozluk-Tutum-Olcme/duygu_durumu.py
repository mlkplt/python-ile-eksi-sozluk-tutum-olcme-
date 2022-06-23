from urllib.error import HTTPError 
from textblob import TextBlob
import time
from tutumu_ölçer import çıktı_al

def scan_file():
    with open("ekşi.txt", "r") as f:
        for line in f.read().split('\n'):
            while True:
                try:
                    blob1= TextBlob(line)
                    blob_eng= blob1.translate(from_lang='tr', to="en")
                except HTTPError:
                    print("\nBağlantı hatası tespit ettik. Tekrar bağlanıyor...")
                    time.sleep(5)
                    continue
                çıktı0=(blob_eng.sentiment_assessments)
                çıktı=round(float(çıktı0[0] * çıktı0[1]) ,2)
                çıktı_al(çıktı)
                break     
