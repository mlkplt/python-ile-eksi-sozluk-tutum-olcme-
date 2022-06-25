import requests
from bs4 import BeautifulSoup

def get_data(url):
    r= requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
    soup= BeautifulSoup(r.content,"lxml")
    return soup