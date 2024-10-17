import  random
def sayi_tahmin_etme_oyunu():
    # Bilgisayar 1 ile 10 arasında rastgele bir sayı seçer
    tutulan_sayi = random.randint(1, 10)
    tahmin = 0

    print("Ben 1 ile 10 arasında bir sayı tuttum.")
    
    # Kullanıcı doğru sayıyı tahmin edene kadar döngü devam eder
    while tahmin != tutulan_sayi:
        try:
            # Kullanıcıdan bir tahmin alınır
            tahmin = int(input("Tahmininizi giriniz: "))

            # Kullanıcının tahmini kontrol edilir
            if tahmin < tutulan_sayi:
                print("Daha büyük bir sayı tahmin etmelisin.")
            elif tahmin > tutulan_sayi:
                print("Daha küçük bir sayı tahmin etmelisin.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")

    print(f"Tebrikler! Doğru tahmin {tutulan_sayi} idi.")


def renk_tahmin_etme_oyunu():
    # Mümkün renklerin listesi
    renkler = ["kırmızı", "turuncu", "sarı", "yeşil", "mavi", "mor"]
    # Bilgisayarın rastgele bir renk seçmesi
    tutulan_renk = random.choice(renkler)

    print("Ben bir renk tuttum. Bu renklerden birini tahmin et: kırmızı, turuncu, sarı, yeşil, mavi, mor.")

    tahmin_sayisi = 0

    # Kullanıcı doğru rengi tahmin edene kadar döngü devam eder
    while True:
        tahmin = input("Tahmininizi giriniz: ").lower()  # Kullanıcı girdisini küçük harfe çevirir
        tahmin_sayisi += 1

        # Kullanıcının tahmini kontrol edilir
        if tahmin == tutulan_renk:
            print(f"Tebrikler! Doğru tahmin. Tutulan renk {tutulan_renk} idi.")
            print(f"Toplam {tahmin_sayisi} tahminde bulundunuz.")
            break
        else:
            print("Yanlış. Tekrar deneyin!")



    