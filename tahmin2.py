import random
import time

print("""*******

1 ile 40 arasındaki sayiyi tahmin edelim.

*********\n""")

rastgele_sayi=random.randint(1,40)
tahmin_hakki=5

while tahmin_hakki > 0:

    print("Kalan tahmin hakkınız {}".format(tahmin_hakki),end="\n"*2)
    tahmin=int(input("tahmininiz:"))
    tahmin_hakki-=1   

    if (tahmin < rastgele_sayi):

        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha yüksek bir sayi söyleyin...",end="\n"*2)

    elif(tahmin > rastgele_sayi):
        print("bilgiler sorgulanıyor....")
        time.sleep(1)
        print("daha düşük bir sayi söyleyin...",end="\n"*2)

    else:
        print("bilgiler sogulanıyor...")
        time.sleep(1)
        print("tebrikler! sayimiz",rastgele_sayi)

        break

else:
    print("Tahmin hakkınız kalmadı.")