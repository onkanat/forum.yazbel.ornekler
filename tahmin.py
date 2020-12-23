### Bu kod https://forum.yazbel.com/t/python-tahmin-oyununda-kod-duzeltmesi/10528/3 alınmıştır.
import time
import random

print("""*******

1 ile 40 arasındaki sayiyi tahmin edelim.

*********\n""")

rastgele_sayi = random.randint(1,40) # 1 ile 40 arasında rastgele int sayı belirler.
tahmin_hakkı=5 # Kullanıcı için tahmin hakkı

while True:

    print("Kalan tahmin hakkınız {}".format(tahmin_hakkı),end="\n"*2)
    tahmin=int(input("tahmininiz:")) 

    if (tahmin < rastgele_sayi): # Tahmin sayıdan küçükse burası çalışır.
        tahmin_hakkı-=1
        
        if (tahmin_hakkı)<1:
            print(" üzgünüm hakkınız bitti")
            print("sayımız:",rastgele_sayi)
            break
        else:
            print("bilgiler sorgulanıyor....")
            time.sleep(1)
            print("daha yüksek bir sayi söyleyin...")
            print(tahmin_hakkı)
            
    elif(tahmin > rastgele_sayi): # Tahmin sayıdan büyükse burası çalışır.
        tahmin_hakkı-=1
         
        if (tahmin_hakkı)<1:
            print(" üzgünüm hakkınız bitti")
            print("sayımız:",rastgele_sayi)
            break
        else:
             print("bilgiler sorgulanıyor....")
             time.sleep(1)
             print("daha düşük bir sayi söyleyin...")             
             print(tahmin_hakkı)
    else:                               # Büyük yada Küçük değil ise burası çalışır.
        print("bilgiler sogulanıyor...")
        time.sleep(1)
        print("tebrikler! sayimiz",rastgele_sayi)
        break