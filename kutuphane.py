# Python 3.9.0
# -*- coding: utf_8 -*-

# class f_ag:------> agirlik hesaplamada
# yuvarlak....................> içi dolu yuvarlak malzeme
# kare................> kare malzemenin
# dortkose............malzemenin
# boru.............malzemenin
# class f_vf:--------> kesme verisi ve işleme zamanları
# class f_geo: ------> pisagor teoremi ile ilgili formuller


import math

# .......................................................

#Sınıfın init fonksiyonuna malzeme adlı bir argüman daha ekledik.
#Böylece aynı sütun yoğunluğuna sahip malzemeler karışmayacak.
class f_ag:
    def __init__(self, OzAgirlik, malzeme):
        self.Oz = OzAgirlik
        self.malzeme = malzeme

    def yuvarlak(self, Cap, Boy): #Yuvarlak malzemenin ağırlığını hesaplar.
        agirlik = ((Cap/2)**2*math.pi*self.Oz*Boy)/1000000
        
        return agirlik

    def kare(self, Kenar, Boy): #Kare malzemenin ağırlığını hesaplar.
        agirlik = Kenar**2*Boy*self.Oz/1000000
        
        return agirlik

    def dortkose(self, En, Boy, Yukseklik): #Dörtköşe malzemenin ağırlığını hesaplar.
        agirlik = En*Boy*Yukseklik*self.Oz/1000000
        
        return agirlik

    def boru(self, DisCap, IcCap, Boy):#Boru malzemenin ağırlığını hesaplar.
        agirlik = (((DisCap**2-IcCap**2)*math.pi*Boy/4)*self.Oz)/1000000
        
        return agirlik
    # çokgen malzeme için formül eklenecek


class f_vf:  # Kesme verisi ve işleme zamanları
    def __init__(self):
        self

    def devir(self, KesmeHizi, Cap): # Kesici/Malzeme dönüş devrini hesaplar
        n = KesmeHizi*1000/math.pi/Cap
        
        return n #print(n, "d/dak")

    def kesmehizi(self, Cap, Devir): # Devri bilinen Kesici/Malzeme kesme hızını hesaplar
        v = math.pi*Cap*Devir/1000
        
        return v #print(v, " m/dak")

    def ilerleme(self, DisSayisi, Fz, Devir): # Diş başına ilerleme ve diş sayısını dikkate alarak
        f = DisSayisi*Fz*Devir                # Takım ilerlemesini hesaplarS
        
        return f #print(f, "mm/dak")

    def alin_torna(self, DisCap, IcCap, KesmeHizi, KesmeIlerlemesi, PasoMiktari, PasoDerinligi, Yanasma):
        
        # KesmeHizi*1000/math.pi/DisCap dev/dak
        Devir = f_vf().devir(KesmeHizi, DisCap)
        Ilerleme = KesmeIlerlemesi*Devir  # mm/dak
        PasoBoyu = (DisCap-IcCap)/2
        # PasoSayisi Tamsayı haline getirilicek
        PasoSayisi = (PasoMiktari/PasoDerinligi)
        PasoSuresi = (((PasoBoyu+Yanasma)*PasoSayisi)/Ilerleme)*60
        return PasoSuresi, PasoSayisi

    def discap_torna(self, HamCap, TornalamaCapi, TornalamaBoyu, KesmeHizi, KesmeIlerlemesi, PasoDerinligi, Yanasma):
        
        Devir = f_vf().devir(KesmeHizi, HamCap)  # KesmeHizi*1000/math.pi/DisCap
        Ilerleme = KesmeIlerlemesi*Devir
        PasoSayisi = ((HamCap-TornalamaCapi)/2)/PasoDerinligi
        PasoSuresi = (PasoSayisi*(TornalamaBoyu+Yanasma))/Ilerleme*60
        return PasoSuresi, PasoSayisi

    def dis_cekme(self, DisAdimi, Devir, DisBoyu, PasoSayisi, Yanasma):
        PasoSuresi = ((DisBoyu+Yanasma)/(Devir*DisAdimi)*PasoSayisi)
        return PasoSuresi

    def delik_delme(self, DelikCapi, DelmeBoyu, KesmeHizi, KesmeIlerlemesi):
        # f_vf....kütüpanesine atıf tt terimi satandart kullanım için yeniden değerlendir
        PasoSuresi = DelmeBoyu/(f_vf().devir(KesmeHizi, DelikCapi)*KesmeIlerlemesi)
        return PasoSuresi

    def yuzey_silme(self, En, Boy, KesmeHizi, TakimCapi, DisSayisi, DisBasinaIlerleme):
        # f_vf....kütüpanesine atıf tt terimi standart kullanım için yeniden değerlendir
        Ilerleme = f_vf().ilerleme(DisSayisi, DisBasinaIlerleme,
                               f_vf().devir(KesmeHizi, TakimCapi))
        # Hesaplamalar takım çapının %70 i için yapılıyor
        PasoSayisi = En/(.70*TakimCapi)
        PasoSuresi = ((PasoSayisi*(Boy+Boy*.70*TakimCapi))/Ilerleme)
        return PasoSuresi

""" #Sabit kesme hızı için Paso zamanı hesaplama formülü??? 
#işleme zamanları için formül geliştir paso_sayısı,paso_boyu
# ilerleme hızı ilişkisi Çap küçüldükçe devri yeniden hesapla
# freze ve tornalama için çap farkı paso miktarı paso sayısı
# hesapla ((ham_çap-tornalama_çap)/2)/paso_derinliği=paso_sayısı
# paso_sayısı*paso_boyu=işleme_boyu
# işleme_boyu/ilerleme=işleme_zamanı (tüm ölçüler mm göre formüle
# edilecek """                


class f_geo:
    def __init__(self):
        self

    def hipotenus(self, kenar1, kenar2):
        """ iki kenar ölçüsü bilinen dik üçgenin hipotenüsünü hesaplar """
        hp = math.sqrt(kenar1**2+kenar2**2)
        print(hp)
        return hp

    def dikucgen(self, karsi, komsu):
        A = (karsi/komsu); Ad = math.atan(A)
        B = komsu/karsi;   Bd = math.atan(B)
        print((math.sqrt(karsi**2+komsu**2), " Hipotenus"))
        print(("A=", math.degrees(Ad), "Derece"))
        print(("B=", math.degrees(Bd), "Derece"))
        print(("tan    A=", A))
        print(("Cosinüs A=", math.cos(Ad)))
        print(("Sinus  A=", math.sin(Ad)))

    def dikucgenh(self, hipotenus, karsi):
        komsu = math.sqrt((hipotenus**2)-(karsi**2))
        A = (karsi/komsu); Ad = math.atan(A)
        print((komsu, "komsu"))
        print(("A=", math.degrees(Ad), "Derece"))
        print(("tan    A=", A))
        print(("Cosinüs A=", math.cos(Ad)))
        print(("Sinus  A=", math.sin(Ad)))

    def daire_alan(self, cap):
        alan = ((cap/2)**2*math.pi)
        print(alan)
        return alan

    def daire_cevre(self, cap):
        cevre = (cap*math.pi)
        print(cevre)
        return cevre
        
    def iki_nokta(self, x1, y1, x2, y2):
        mesafe = math.sqrt((x1-x2)**2+(y1-y2)**2)
        return mesafe