import random
import matplotlib.pyplot as plt

class Esya:
    def __init__(self, esyaAgirlik, esyaDeger):
        self.esyaAgirlik = esyaAgirlik
        self.esyaDeger = esyaDeger

def rastgeleVeriSetiOlustur(esyaSayisi):
    # Belirtilen sayıda rastgele eşyalar oluşturulur.
    esyalar = []
    for _ in range(esyaSayisi):
        agirlik = random.randint(1, 20)  # Eşyanın rastgele ağırlığı belirlenir.
        deger = random.randint(10, 20)   # Eşyanın rastgele değeri belirlenir.
        esya = Esya(agirlik, deger)       # Eşya nesnesi oluşturulur ve listeye eklenir.
        esyalar.append(esya)
    return esyalar

def hesaplaMaliyet(birey, esyalar, maxAgirlik):
    # Verilen bir bireyin maliyetini hesaplar.
    toplamDeger = 0
    toplamAgirlik = 0
    for i in range(len(birey)):
        if birey[i] == 1:
            toplamDeger += esyalar[i].esyaDeger   # Eşyanın değeri toplam değere eklenir.
            toplamAgirlik += esyalar[i].esyaAgirlik  # Eşyanın ağırlığı toplam ağırlığa eklenir.
    if toplamAgirlik > maxAgirlik:
        toplamDeger = 0   # Ağırlık sınırını aşan bir durumda maliyet sıfırlanır.
    return toplamDeger

def kelebekOptimizasyonu(esyalar, maxAgirlik, maxIterasyon, kelebekSayisi):
    # Kelebek optimizasyonu algoritması ile en iyi kombinasyonu bulma işlemi gerçekleştirilir.
 
    #Kelebeklerin pozisyonlarını temsil eden "kelebekler" listesi
    kelebekler = [[random.randint(0, 1) for _ in range(len(esyalar))] for _ in range(kelebekSayisi)]
    # Kelebeklerin başlangıç pozisyonları rastgele belirlenir.

    enIyiBirey = []  # En iyi bireyin başlangıç değeri
    enIyiMaliyet = 0  # En iyi maliyetin başlangıç değeri

    enIyiMaliyetDegerleri = []  # Iterasyonlar boyunca en iyi maliyetin değerlerinin tutulduğu liste
    iterasyonlar = []  # Iterasyon sayılarının tutulduğu liste

    for iterasyon in range(maxIterasyon):
        # Kelebeklerin değerlendirilmesi
        maliyetler = [hesaplaMaliyet(kelebek, esyalar, maxAgirlik) for kelebek in kelebekler]
        # Her kelebeğin maliyeti hesaplanır.

        # En iyi bireyin seçimi
        enIyiMaliyet = max(maliyetler)  # En yüksek maliyet bulunur
        enIyiBirey = kelebekler[maliyetler.index(enIyiMaliyet)]  # En iyi bireyin indeksi ile seçilir

        enIyiMaliyetDegerleri.append(enIyiMaliyet)  # En iyi maliyet değeri listeye eklenir
        iterasyonlar.append(iterasyon + 1)  # İterasyon sayısı listeye eklenir

        # Kelebeklerin hareketi ve etkileşimi
        for i in range(kelebekSayisi):
            yeniKelebek = [] #"yeniKelebek" adında boş bir liste oluşturulur.
            for j in range(len(esyalar)): #Kelebeklerin genetik özelliklerini temsil eden "kelebekler"
            #listesinin her bir elemanını dolaşan iç içe 
            #bir döngü başlatılır. Bu iç döngü, eşya sayısı kadar tekrarlanır.
                if random.random() < 0.5: #Her bir genetik özelliğin (0 veya 1) korunma veya değiştirme olasılığı hesaplanır. 
                #Bu, random.random() < 0.5 ifadesiyle yapılır. random.random() 0 ile 1 arasında rastgele bir sayı döndürür.
                #Eğer bu sayı 0.5'ten küçükse, genetik özellik korunur ve aynı şekilde yeni kelebek listesine eklenir. 
                #Eğer 0.5'ten büyükse, genetik özellik değiştirilir ve 0 ise 1, 1 ise 0 olarak yeni kelebek listesine eklenir.
                    yeniKelebek.append(kelebekler[i][j])
                else:
                    yeniKelebek.append(1 - kelebekler[i][j])
            kelebekler[i] = yeniKelebek
            # Kelebeklerin hareketi ve etkileşimi gerçekleştirilir.

    print("---Sonuç ---")
    print("Optimizasyon Sonu:")
    print("En iyi Maliyet:", enIyiMaliyet)
    print("En iyi Birey:", enIyiBirey)

    # Grafik
    plt.plot(iterasyonlar, enIyiMaliyetDegerleri)
    plt.xlabel("Iterasyonlar")
    plt.ylabel("En İyi Maliyet Değeri :")
    plt.title("Kelebek Optimizasyonu Sırt Çantası Uygulaması")
    plt.grid(True)
    plt.show()

def main():
    esyaSayisi = 6
    esyalar = rastgeleVeriSetiOlustur(esyaSayisi)
    
    # Oluşturulan veri setini yazdırma
    for esya in esyalar:
        print("Eşya Ağırlığı:", esya.esyaAgirlik, "- Eşya Değeri:", esya.esyaDeger)

    maxAgirlik = 50
    maxIterasyon = 5
    kelebekSayisi = 10

    kelebekOptimizasyonu(esyalar, maxAgirlik, maxIterasyon, kelebekSayisi)

if __name__ == "__main__":
    main()
