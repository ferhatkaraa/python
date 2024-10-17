




matris = [[2,2,3],[2,0,3],[2,2,0]]
def matris_çöz(çöz):
    sonuç = 0
    #kare matris mi
    if len(çöz) == len(çöz[0]):  
        yeni_matrsiler = dict()
        if len(çöz) > 2:
            for i in range(len(çöz[0])):
                son_matris = list()
                #ilk satır seçildi
                for j in çöz[1:]:
                    satır = list()
                    for k in range(len(j)):
                        #k = i ise aynı sütun demek 
                        # o yüzden aynı sütun olan sütun atlanır
                        if k == i:
                            continue
                        satır.append(j[k])
                    #hesaplamada kullanılıcak sayılar alınır
                    #bir alt matrise geçilir
                    son_matris.append(satır)
                    del(satır)
                #matrisin kuralına göre işaret ve seçilen satırın elemanı alınır
                #alt matris ise tekrar fonksiyona gönderilir
                sonuç += ((-1)**i)*çöz[0][i]*matris_çöz(son_matris)
                del(son_matris)
            return sonuç
                        
                    
        elif len(çöz) == 2:
            sonuç_çöz = çöz[0][0]*çöz[1][1] - çöz[0][1]*çöz[1][0]
            return sonuç_çöz
        else:
            print("bir sorun oluştu \n matrisin satır sayısı:",len(çöz))
            
print(matris_çöz(matris))
            
