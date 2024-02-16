'''
--Yunus Sürüsü Optimizasyonu (DSO - Dolphin Swarm Optimization), 
yunusların avlanma ve sosyal davranışlarından ilham alınarak geliştirilen bir optimizasyon algoritmasıdır. 
Bu algoritma, yunusların avlarını sürü halinde nasıl etkili bir şekilde avladıklarını ve birbirleriyle nasıl iletişim kurduklarını modelleyerek karmaşık problemlerin çözümünde kullanılır. 
DSO, genellikle global optimizasyon problemlerinde kullanılır ve çeşitli mühendislik, araştırma ve geliştirme problemlerinde etkili çözümler üretmek için uygulanabilir.



--- DSO'nun Temel Prensipleri
1) Eşitleme Davranışı (Echolocation Behavior): 
Yunusların çevrelerini sese dayalı olarak algılamaları. 
Bu, DSO'da bir arama alanı içindeki çözüm adaylarının konumlarını belirlemek için kullanılır.



2) Sürü Davranışı (Swarm Behavior): 
Yunuslar, avlarını çevreleyerek ve onları daha küçük bir alana sıkıştırarak avlarlar. 
DSO, bu davranışı optimizasyon sürecinde, çözümleri potansiyel en iyi çözüme doğru yönlendirerek modellemektedir.


3) İletişim ve İşbirliği: 
Yunuslar, birbirleriyle karmaşık sesler aracılığıyla iletişim kurarlar. 
DSO'da, bu, çözüm adaylarının birbirleriyle bilgi paylaşmasını ve işbirliği yapmasını sağlayarak optimizasyon sürecini güçlendirir.



-- DSO Algoritmasının Adımları
DSO algoritması, genellikle aşağıdaki adımları içerir:

1) Başlangıç Popülasyonunun Oluşturulması: 
Rastgele seçilen çözüm adaylarıyla bir başlangıç popülasyonu oluşturulur.


2) Eşitleme ve Arama: 
Her yunus (çözüm adayı), çevresindeki çözümleri değerlendirerek daha iyi çözümlere doğru hareket eder.


3) Sürü Oluşturma ve Avlanma: 
En iyi çözümler etrafında sürüler oluşturulur ve çözümler bu en iyi noktalara doğru yönlendirilir.


4) Güncelleme ve İterasyon: 
Popülasyon, belirli bir durma kriteri karşılanana kadar güncellenir ve iterasyonlar devam eder.



'''




import numpy as np

# Hedef fonksiyon: Bu örnekte, basit bir kare fonksiyonunu minimizasyoruz.
def objective_function(x):
    return x**2

# DSO algoritmasının ana fonksiyonu
def dolphin_swarm_optimization(objective, bounds, population_size, iterations):
    # Başlangıç popülasyonunu oluştur
    population = np.random.uniform(bounds[0], bounds[1], (population_size, 1))
    best_solution = population[0]
    best_score = objective(best_solution)
    
    # Her iterasyonda...
    for i in range(iterations):
        # Her yunus için...
        for j in range(population_size):
            candidate_solution = population[j] + np.random.normal(0, 1)
            candidate_score = objective(candidate_solution)
            
            # Eğer daha iyi bir çözüm bulunursa, güncelle
            if candidate_score < best_score:
                best_solution = candidate_solution
                best_score = candidate_score
        
        # Bilgi çıktısı
        print(f'Iterasyon {i+1}, En İyi Skor: {best_score}')
    
    return best_solution, best_score

# Parametreler
bounds = (-10, 10)  # Arama alanı
population_size = 30  # Popülasyon büyüklüğü
iterations = 100  # İterasyon sayısı

# DSO algoritmasını çalıştır
best_solution, best_score = dolphin_swarm_optimization(objective_function, bounds, population_size, iterations)
print(f'En iyi çözüm: {best_solution}, Skor: {best_score}')
