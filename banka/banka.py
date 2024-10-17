







kayıt = dict()
print("**********************************************************************************************************************")
print("HOŞGELDİNİZ")
while True:
    for i,j in kayıt.items():
        print(i,"--->",j)
    try:
        giriş = input("1-hesap aç\n2-hesaba gir\n3-uygulamayı kapat")
        if giriş == "1":
            print("KAYIT EKRANI\n----------------------------------------------------")
            hesap = input("hesap adını girin")
            if hesap not in kayıt.keys():
                kayıt[hesap] = int(input("hesabına ne kadar para eklemek istersin?"))
            else:
                print("bu hesap adı zaten var")
        elif giriş == "2":
            print("GİRİŞ EKRANI\n----------------------------------------------------")
            hesap = input("hesap adını girin")
            if hesap in kayıt.keys():
                işlem = input("1-para çek\n2-para yatır\n3-başka hesaba para aktar\n işlem türünü seçin")
                if işlem == "1":
                   kayıt[hesap] -= int(input("hesabından ne kadar para çekmek istersin?"))
                elif işlem == "2":
                    kayıt[hesap] += int(input("hesabına ne kadar para yatırmak istersin?"))

                elif işlem == "3":
                    aktar = input("kimin hesabına para yatırmak istersin?")
                    para = int(input("ne kadar para aktarmak istersin"))
                    kayıt[aktar] += para
                    kayıt[hesap] -= para
                else:
                    print("hatalı işlem kodu girdiniz")
            else:
                print("bu kullanıcı adı hatalı")
        else:
            print("görüşmek üzere")
            break
    except:
        print("bir hata oluştu")
        break
















print("**********************************************************************************************************************")