'''
PSO'nun Çalışma Prensibi
1. Başlangıç Durumu: Algoritma, her biri bir çözümü temsil eden rastgele konumlandırılmış parçacıklarla başlar.
Her parçacık, bir hız vektörüne sahiptir ve bu, parçacığın çözüm alanındaki hareket yönünü ve hızını belirler.

2. Değerlendirme: Her bir parçacığın konumu, bir amaç (fitness) fonksiyonu kullanılarak değerlendirilir.
 Bu fonksiyon, parçacığın mevcut çözümünün kalitesini ölçer.

 

3. Kişisel ve Global En İyi Değerler: Her parçacık, kendi deneyimindeki en iyi konumu (kişisel en iyi) ve sürüdeki tüm parçacıklar arasındaki en iyi konumu (global en iyi) saklar.

4. Hız ve Konum Güncellemesi: Her iterasyonda, parçacıkların hızları ve konumları, hem kendi kişisel en iyi konumlarına hem de sürünün global en iyi konumuna doğru bir yönelim göstererek güncellenir. Bu, parçacıkların potansiyel olarak daha iyi çözümlere doğru "öğrenmelerini" ve "hareket etmelerini" sağlar.

5. Sonlanma Kriteri: Algoritma, belirlenen bir iterasyon sayısına ulaştığında veya başka bir sonlanma kriteri karşılandığında sona erer.

'''

'''
PSO, mühendislikten finansa, yapay zekâ uygulamalarından işletme problemlerine kadar geniş bir yelpazede optimizasyon problemlerinde kullanılabilir. 
Şimdi, basit bir PSO kod örneği üzerinden bu algoritmanın nasıl implemente edilebileceğini göstereceğim.

PSO algoritmasının basit bir Python implementasyonu sonucunda, amaç fonksiyonu olarak tanımladığımız ( x**2 + y**2) fonksiyonunu minimizasyon probleminde,
 global en iyi çözümün konumu yaklaşık olarak [4.27 x 10**-5, -1.59x10**-4]   olarak bulunmuştur ve bu konumdaki amaç fonksiyonunun değeri 2.72 x 10**-8'dir.
 Bu sonuç, algoritmanın başarılı bir şekilde çalıştığını ve global minimuma çok yakın bir noktada sonlandığını göstermektedir. 
 Bu örnekte, algoritmanın parametreleri (atalet ağırlığı, kişisel ve sosyal katsayılar, iterasyon sayısı) basit tutulmuş olup, farklı problemlere ve durumlara göre bu parametrelerin ayarlanması gerekebilir

'''




# PSO'nun basit bir Python implementasyonu
import numpy as np

# Amaç fonksiyonu: Sphere fonksiyonu - x^2 + y^2 minimizasyonu
def objective_function(X):
    return np.sum(X ** 2, axis=1)

# PSO parametreleri
n_particles = 30
n_dimensions = 2
x_min, x_max = -10, 10
v_max = (x_max - x_min) * 0.2
iterations = 100
w = 0.7  # atalet ağırlığı
c1, c2 = 2.05, 2.05  # kişisel ve sosyal katsayılar

# Parçacıkların başlangıç konumları ve hızları
X = np.random.uniform(low=x_min, high=x_max, size=(n_particles, n_dimensions))
V = np.random.uniform(low=-v_max, high=v_max, size=(n_particles, n_dimensions))

# Kişisel en iyi konumlar ve değerler
P_best = X.copy()
P_best_val = objective_function(X)

# Global en iyi konum ve değer
G_best_idx = np.argmin(P_best_val)
G_best = X[G_best_idx, :].copy()
G_best_val = P_best_val[G_best_idx]

# PSO döngüsü
for i in range(iterations):
    # Hız güncellemesi
    r1, r2 = np.random.rand(n_particles, n_dimensions), np.random.rand(n_particles, n_dimensions)
    V = w*V + c1*r1*(P_best - X) + c2*r2*(G_best - X)
    V = np.clip(V, -v_max, v_max)  # Hız sınırlaması
    
    # Konum güncellemesi
    X += V
    X = np.clip(X, x_min, x_max)  # Konum sınırlaması
    
    # Değerlendirme ve en iyi değerlerin güncellenmesi
    current_val = objective_function(X)
    better_mask = current_val < P_best_val
    P_best[better_mask] = X[better_mask].copy()
    P_best_val[better_mask] = current_val[better_mask]
    
    # Global en iyi güncellemesi
    G_best_idx_new = np.argmin(P_best_val)
    if P_best_val[G_best_idx_new] < G_best_val:
        G_best = P_best[G_best_idx_new, :].copy()
        G_best_val = P_best_val[G_best_idx_new]

# Sonuç
print (G_best, G_best_val)
