'''
--Yapay Bağışıklık Sistemleri (AIS - Artificial Immune Systems),
biyolojik bağışıklık sistemlerinin davranışlarını taklit eden bilgisayar algoritmalarıdır. 
Bu sistemler, özellikle tanıma, öğrenme, hafıza ve kendini iyileştirme yeteneklerini modellemek için kullanılır. 
AIS, özellikle desen tanıma, anormallik tespiti ve fonksiyon optimizasyonu gibi alanlarda kullanılmaktadır.


AIS'in Temel Bileşenleri ve Mekanizmaları
Yapay Bağışıklık Sistemleri, aşağıdaki biyolojik mekanizmalardan ilham alır:

* Antijenler (Ag): Sisteme zarar verebilecek herhangi bir dış etken veya girdi.

* Antikorlar (Ab): Antijenleri tanıyıp bağlanarak onları etkisiz hale getiren protein molekülleri. AIS'de, çözüm adaylarını veya durumu temsil eder.

* Afinite: Antikorların antijenlere ne kadar iyi bağlandığının bir ölçüsü. Genellikle uygunluk fonksiyonu ile modellenir.

* Klonal Seçilim: En iyi antikorların (en yüksek afiniteye sahip olanların) seçilip klonlanması ve mutasyona uğratılması işlemidir. 
Bu, arama alanında çeşitliliği ve optimal çözüme ulaşmayı sağlar.

* Hafıza Hücreleri: Geçmişte karşılaşılan antijenlere hızlı yanıt vermek üzere saklanan antikorlar. Sistemin öğrenme ve hafıza yeteneğini temsil eder.



-- Basit Bir AIS Algoritması
1) Başlangıç Popülasyonunun Oluşturulması: Rastgele antikorlar (çözüm adayları) üretilir.
2) Afinite Değerlendirmesi: Her antikor için afinite (uygunluk) hesaplanır.
3) Klonal Seçilim: En iyi antikorlar seçilir ve klonlanır. Klon sayısı, antikorun afinite değerine bağlıdır.
4) Mutasyon: Klonlanan antikorlar, çeşitliliği artırmak için mutasyona uğratılır. Mutasyon oranı, genellikle antikorun afinite değerine ters orantılıdır.
5) Hafıza Güncellemesi: En iyi antikorlar hafıza hücrelerine eklenir veya güncellenir.
6) Yeni Popülasyonun Oluşturulması: Yeni antikorlar (çözümler) rastgele veya mevcut antikorlardan türetilerek oluşturulur.
7) Terminasyon Kriteri: Belirlenen iterasyon sayısına ulaşılıncaya veya başka bir durdurma kriteri karşılanıncaya kadar adımlar tekrarlanır.
'''

import numpy as np

# Antikor sınıfı: Çözüm adaylarını temsil eder
class Antibody:
    def __init__(self, genes):
        self.genes = genes  # Antikorun genleri (çözümün parçaları)
        self.affinity = 0  # Afinite (uygunluk) değeri

# Afinite (uygunluk) fonksiyonu: Basit bir örnek
def affinity_function(antibody):
    # Afinite, genlerin toplamı olarak hesaplanır (basitleştirilmiş bir örnek)
    return sum(antibody.genes)

# Başlangıç popülasyonunu oluşturma
def create_initial_population(size, gene_length):
    return [Antibody(np.random.rand(gene_length)) for _ in range(size)]

# Klonal seçilim ve mutasyon
def clonal_selection_and_mutation(antibodies, clone_factor, mutation_rate):
    clones = []
    for ab in antibodies:
        for _ in range(int(clone_factor * ab.affinity)):  # Afiniteye bağlı klon sayısı
            cloned_ab = Antibody(ab.genes.copy())
            # Mutasyon: Genlerin bir kısmını rastgele değiştir
            mutation_indices = np.random.choice(range(len(ab.genes)), size=int(mutation_rate * len(ab.genes)), replace=False)
            cloned_ab.genes[mutation_indices] = np.random.rand(len(mutation_indices))
            clones.append(cloned_ab)
    return clones

# Ana algoritma
def ais_algorithm(population_size=100, gene_length=10, clone_factor=0.1, mutation_rate=0.05, iterations=100):
    # Başlangıç popülasyonunu oluştur
    population = create_initial_population(population_size, gene_length)
    for iteration in range(iterations):
        # Afiniteyi hesapla
        for ab in population:
            ab.affinity = affinity_function(ab)
        # En iyi antikorları seç
        population.sort(key=lambda ab: ab.affinity, reverse=True)
        selected_antibodies = population[:int(0.2 * population_size)]
        # Klonlama ve mutasyon
        clones = clonal_selection_and_mutation(selected_antibodies, clone_factor, mutation_rate)
        # Yeni popülasyon
        population = clones + create_initial_population(population_size - len(clones), gene_length)
    return population

# Algoritmayı çalıştır ve en iyi çözümü bul
final_population = ais_algorithm()
best_solution = max(final_population, key=lambda ab: ab.affinity)
print("En iyi çözüm:", best_solution.genes, "Afinite:", best_solution.affinity)
