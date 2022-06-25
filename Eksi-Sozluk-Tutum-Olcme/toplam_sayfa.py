from data import get_data

def toplamSayfa(url):
    soup= get_data(url)
    try:
        toplam_sayfa= soup.find("div", {"class":"clearfix sub-title-container"}).find("div",{"class":"pager"})["data-pagecount"]
    except:
        toplam_sayfa=1
        print("Toplam sayfa sayısı 1'den küçük!")
    return int(toplam_sayfa)