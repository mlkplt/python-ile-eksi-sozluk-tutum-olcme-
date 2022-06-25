from bs4 import BeautifulSoup
from toplam_sayfa import toplamSayfa
import time
import requests

def file_write(url,file):
    a=1
    print("\nİçerik alınıyor... Bekleyin...")
    for sayfaR in range(1, toplamSayfa(url)+1):
        sayfaR= requests.get(url, str("a=nice&p=")+str(a), headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
        soup1= BeautifulSoup(sayfaR.content,"lxml")

        for içerik in soup1.find_all("div", {"class": "content"}):
            dosya=içerik.text.strip()
            # file.write(str("*")+" "+ str(dosya)+"\n\n")
            file.write(dosya)      
        a=a+1
    print("\nİçerik alma işlemi tamamlandı...")
    time.sleep(1)
    file.close()