'''
Ateşböceği Algoritması (Firefly Algorithm), doğadaki ateşböceklerinin davranışlarından ilham alınarak geliştirilmiş bir optimizasyon algoritmasıdır. 
Bu algoritma, özellikle sürekli optimizasyon problemlerinin çözümünde kullanılır. 
Ateşböceklerinin birbirlerini çekici bulmalarının temel sebebi, ışık yaymalarıdır. 
Algoritmanın temel prensibi de benzer şekilde, çözüm adaylarının birbirlerini çekmesi ve bu çekim kuvvetinin çözümlerin kalitesine bağlı olarak değişmesidir. 
Daha iyi çözümler daha fazla "ışık" yayarak, diğer çözümleri kendilerine doğru çeker.


--- Ateşböceği Algoritmasının Temel Adımları:

1) Başlangıç Popülasyonunun Oluşturulması: 
Rastgele seçilen çözümlerle bir başlangıç popülasyonu oluşturulur.



2) Parlaklık Değerinin Hesaplanması: 
Her bir ateşböceğinin parlaklığı (çekiciliği), çözümün kalitesine (uygunluk değerine) bağlıdır.



3) Ateşböceklerinin Hareketi: 
Her bir ateşböceği, kendisinden daha parlak olan diğer ateşböceklerine doğru hareket eder. 
Bu hareket, çekicilik derecesine ve uzaklığa bağlıdır.



4) Güncelleme ve Seçim: 
Hareketler sonucunda elde edilen yeni çözümler değerlendirilir ve popülasyon güncellenir.


5) Durma Kriteri: 
Belirlenen iterasyon sayısına ulaşılana kadar veya başka bir durma kriteri karşılanana kadar 2-4 adımları tekrarlanır.

'''
import numpy as np

# Ateşböceği Algoritmasının Basit Bir Uygulaması

def objective_function(x):
    """Hedef fonksiyonumuz: Burada örnek olarak bir küresel fonksiyon kullanıyoruz.
    x: Çözüm vektörü."""
    return sum(x**2)

def firefly_algorithm(objective, n_dim, n_fireflies=25, alpha=0.5, beta0=1.0, gamma=1.0, max_gen=100):
    """
    Ateşböceği Algoritması
    objective: Hedef fonksiyon.
    n_dim: Çözümün boyutu.
    n_fireflies: Ateşböceği sayısı.
    alpha: Adım büyüklüğü.
    beta0: Çekim kuvvetinin başlangıç değeri.
    gamma: Işık emilim katsayısı.
    max_gen: Maksimum iterasyon sayısı.
    """
    # Başlangıç popülasyonunu rastgele oluştur
    population = np.random.rand(n_fireflies, n_dim)
    light_intensity = np.zeros(n_fireflies)
    best_solution = population[0]
    best_intensity = objective(best_solution)
    
    # Her ateşböceğinin ışık yoğunluğunu hesapla
    for i in range(n_fireflies):
        light_intensity[i] = objective(population[i])
        if light_intensity[i] < best_intensity:
            best_solution = population[i]
            best_intensity = light_intensity[i]
    
    # Ana döngü
    for gen in range(max_gen):
        for i in range(n_fireflies):
            for j in range(n_fireflies):
                if light_intensity[i] > light_intensity[j]: # Daha parlaksa çekime uğra
                    r = np.linalg.norm(population[i] - population[j])
                    beta = beta0 * np.exp(-gamma * r ** 2)
                    population[i] += beta * (population[j] - population[i]) + alpha * (np.random.rand(n_dim) - 0.5)
                    light_intensity[i] = objective(population[i])
                    if light_intensity[i] < best_intensity:
                        best_solution = population[i]
                        best_intensity = light_intensity[i]
    
    return best_solution, best_intensity

# Algoritmayı çalıştır
n_dim = 5 # Çözümün boyutu
best_solution, best_intensity = firefly_algorithm(objective_function, n_dim)

print (best_solution, best_intensity)



'''
Ateşböceği Algoritması ile gerçekleştirdiğimiz optimizasyonun sonucunda, 5 boyutlu bir optimizasyon problemi için en iyi çözüm ve bu çözümün hedef fonksiyon değeri elde edildi. 
Elde edilen en iyi çözüm vektörü [-0.0266033, 0.00660746, -0.00531903, -0.0199713, 0.00016617] şeklindedir ve bu çözümün hedef fonksiyon değeri 0.0011785664200261894 olarak hesaplanmıştır.
Bu değer, seçtiğimiz hedef fonksiyon olan küresel fonksiyon (sum(x^2)) için elde edilebilecek minimum değerlere yakın bir sonuçtur ve
algoritmanın optimizasyon problemine başarılı bir şekilde yakınsadığını gösterir.
'''

'''
Yukarıdaki kodda, algoritmanın temel adımları şu şekilde gerçekleştirilmiştir:

1) Başlangıç Popülasyonunun Oluşturulması: Rastgele seçilen çözümlerle bir başlangıç popülasyonu oluşturulmuştur.


2) Parlaklık Değerinin Hesaplanması: Her bir ateşböceğinin parlaklığı, hedef fonksiyon kullanılarak hesaplanmıştır.


3) Ateşböceklerinin Hareketi: Her bir ateşböceği, kendisinden daha parlak olan diğer ateşböceklerine doğru bir hareket gerçekleştirmiştir. 
Bu hareket, belirlenen çekim kuvveti ve adım büyüklüğüne göre ayarlanmıştır.


4) Güncelleme ve Seçim: Her iterasyonda, ateşböceklerinin konumları güncellenmiş ve en iyi çözüm takip edilmiştir.


5) Durma Kriteri: Belirlenen maksimum iterasyon sayısına (bu örnekte 100) ulaşıldığında algoritma sonlandırılmıştır.


Bu basit uygulama, Ateşböceği Algoritmasının temel prensiplerini ve bir optimizasyon problemine nasıl uygulanabileceğini göstermektedir. 
Gerçek dünya problemlerinde, algoritmanın parametreleri (örneğin, alpha, beta0, gamma, ve n_fireflies) problemin doğasına ve karmaşıklığına göre ayarlanmalıdır.


'''