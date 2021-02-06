
# Dosya adına sıralı numara ekleme ve oluşturulan dosya adlarını
# csv dosya formatında kaydetmek için yazılmıştır.
# Hakan KILIÇASLAN 01/02/2021

import os
from os import path
import csv

filename = ""
csvfilename = "F16_CSV.csv"
ls = []
count = 0
#frm kaydedilen .jpg dosyaların numaralandırılması için kullanılır.
#dosyaların .csv dosyası yaratılır
#path değişkenine dosyaların bulunduğu klasör tanımlanır.
#filename değişkeni yeni dosya isimlerine göre düzenlenir.
#csvfilename değişkeni dosya isimlerine göre tanımlanır
path = "C:\\Users\\user\\Documents\\Python Scripts\\F16\\frm"
for f in os.listdir(path):
    old = os.path.join(path,f)
    filename ="F16frame%d.jpg" % count;count+=1
    #os.rename(old,filename)
    ls.append([filename,1])
    print(old,filename)
    
with open(csvfilename, 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(ls)
writeFile.close
# print(ls)