import time
import random

my_str = """""
Adana ; 01

Adıyaman ; 02

Afyonkarahisar ; 03

Ağrı ; 04

Amasya ; 05

Ankara ; 06

Antalya ; 07

Artvin ; 08

Aydın ; 09

Balıkesir ; 10

Bilecik ; 11

Bingöl ; 12

Bitlis ; 13

Bolu ; 14

Burdur ; 15

Bursa ; 16

Çanakkale ; 17

Çankırı ; 18

Çorum ; 19

Denizli ; 20

Diyarbakır ; 21

Edirne ; 22

Elazığ ; 23

Erzincan ; 24

Erzurum ; 25

Eskişehir ; 26

Gaziantep ; 27

Giresun ; 28

Gümüşhane ; 29

Hakkari ; 30

Hatay ; 31

Isparta ; 32

İçel (Mersin) ; 33

İstanbul ; 34

İzmir ; 35

Kars ; 36

Kastamonu ; 37

Kayseri ; 38

Kırklareli ; 39

Kırşehir ; 40

Kocaeli ; 41

Konya ; 42

Kütahya ; 43

Malatya ; 44

Manisa ; 45

Kahramanmaraş ; 46

Mardin ; 47

Muğla ; 48

Muş ; 49

Nevşehir ; 50

Niğde ; 51

Ordu ; 52

Rize ; 53

Sakarya ; 54

Samsun ; 55

Siirt ; 56

Sinop ; 57

Sivas ; 58

Tekirdağ ; 59

Tokat ; 60

Trabzon ; 61

Tunceli ; 62

Şanlıurfa ; 63

Uşak ; 64

Van ; 65

Yozgat ; 66

Zonguldak ; 67

Aksaray ; 68

Bayburt ; 69

Karaman ; 70

Kırıkkale ; 71

Batman ; 72

Şırnak ; 73

Bartın ; 74

Ardahan ; 75

ığdır ; 76

Yalova ; 77

Karabük ; 78

Kilis ; 79

Osmaniye ; 80

Düzce ; 81
"""
#eldeki string formatlı dataynın dict formatına çevrilmesi
yeni_str = dict()
for i in range(1,82):
    yeni_str[my_str[1:my_str.find(";")]] = i
    my_str = my_str[my_str.find("\n\n")+1:]

    



def main():
    d = 0
    y = 0
    süre = 600
    sınav = input("1-şehirler\n2-plakalar\n3-çıkış\n")
    if sınav == "1":
        liste_city = list(yeni_str.keys())
        #hedef 10 dakikada 50 soruya cevap vermek
        for i in range(1,51):
            baslangic = int(time.time())
            print("kalan süre:",süre)
            soru = random.choice(liste_city)
            liste_city.pop(liste_city.index(soru))#sorulan şehrin tekrar sorulamsını istemiyoruz
            print("------------------------------------------------")
            
            cevap = input(f"{soru} ilinin plakası nedir?")
            bitis = int(time.time())
            süre -= (bitis-baslangic)
            #data içerisinde büyük harf bulunmasından 
            # ve kullanıcının büyük harf kullanma ihtimalinden 
            # dolayı önce küçültme işlemi ardından da kontrol sağlanır
            if str(yeni_str[soru]).lower() == cevap.lower():
                print("doğru cevap")
                d += 1
            else:
                print("yanlış cevap")
                y += 1
            if süre <= 0:
                print("süre bitti")
                if d + y != 50:
                    print("boş sayısı-->",50-d-y)
                break
            print("------------------------------------------------")
        print("doğru--->",d,"yanlış--->",y,"\n","kullanılan toplam süre:",600-süre)
    elif sınav == "2":
        plaka_liste = list(range(1,82))
        #50 soru sorulacak
        for i in range(1,51):
            baslangic = int(time.time())
            print("kalan süre:",süre)
            soru = random.choice(plaka_liste)
            plaka_liste.pop(plaka_liste.index(soru))#sorulan plaka tekrar sorulmasın diye listeden atılıyor
            print("------------------------------------------------")
            
            cevap = input(f"{soru} plakası hangi ile aittir?")
            bitis = int(time.time())
            süre -= (bitis-baslangic)
            #cevabın doğruluğu kontrol ediliyor
            for j in yeni_str.keys():
                if str(yeni_str[j]) == str(soru):
                    if cevap.lower() == i.lower():
                        print("doğru cevap")
                        d += 1
                    else:
                        print("yanlış cevap")
                        y += 1
            if süre <= 0:
                print("süre bitti")
                if d + y != 50:
                    print("boş sayısı-->",50-d-y)
                break
            print("------------------------------------------------")
        print("doğru--->",d,"yanlış--->",y,"\n","kullanılan toplam süre:",600-süre)
    else:
        print("görüşmek üzere")
        
main()