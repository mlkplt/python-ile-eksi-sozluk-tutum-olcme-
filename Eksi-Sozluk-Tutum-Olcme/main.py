#!/usr/bin/env python3
# Path: main.py
#@author: @mlkplt
from dosya_yazımı import file_write
from duygu_durumu import scan_file

def main():
    url= str(input("\nEkşi sözlük linkini girin: "))#içeriğini taramak istediğiniz başlığın linkini kopyalayıp yapıştırın...
    file= open("ekşi.txt","w")
    file_write(url,file)
    scan_file()
    input("\nProgramdan çıkmak için enter'a basın!")
main()
