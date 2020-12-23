### Bu kod https://forum.yazbel.com/t/python-tahmin-oyununda-kod-duzeltmesi/10528/3 alınmıştır.
import time
import random

print("""*******

1 ile 40 arasındaki sayiyi tahmin edelim.

*********\n""")

rastgele_sayi = random.randint(1,40) # 1 ile 40 arasında rastgele int sayı belirler.
tahmin_hakki=5 # Kullanıcı için tahmin hakkı

while tahmin_hakki > 0:

    print("Kalan tahmin hakkınız {}".format(tahmin_hakki),end="\n"*2)
    tahmin=int(input("tahmininiz:"))
    tahmin_hakki-=1 

    if (tahmin < rastgele_sayi): # Tahmin sayıdan küçükse burası çalışır.
        
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha YÜKSEK bir sayi söyleyin...")
                        
    elif(tahmin > rastgele_sayi): # Tahmin sayıdan büyükse burası çalışır.
        
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha DÜŞÜK bir sayi söyleyin...")             
             
    else:                               # Büyük yada Küçük değil ise burası çalışır.
        print("bilgiler sogulanıyor...")
        time.sleep(1)
        print("tebrikler! sayimiz",rastgele_sayi)
        break

else:
    print(" üzgünüm hakkınız bitti")
    print("sayımız:",rastgele_sayi)