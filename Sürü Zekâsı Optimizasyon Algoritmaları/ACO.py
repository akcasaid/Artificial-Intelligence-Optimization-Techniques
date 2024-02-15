'''
Karınca Koloni Optimizasyonu (ACO), yapay zekâ ve optimizasyon problemlerinde sıkça kullanılan bir algoritmadır. 
Bu algoritma, gerçek dünyadaki karınca kolonilerinin davranışlarından esinlenerek geliştirilmiştir. 
Karıncalar, yiyecek bulma ve en kısa yolu bulma konusunda etkileyici bir yeteneğe sahiptir. 
Bu yetenek, karıncaların birbirleriyle ve çevreleriyle etkileşim kurarak bilgi paylaşımı yapmalarından kaynaklanır. 
ACO, bu doğal davranışı matematiksel bir modelle taklit eder ve çeşitli optimizasyon problemlerinin çözümünde kullanılır.


----- ACO'nun Temel Prensipleri -----

1) Feromon Biriktirme: 
Karıncalar, geçtikleri yolda feromon adı verilen kimyasal izler bırakır. 
Bu izler, diğer karıncaların yolu takip etmesine yardımcı olur. ACO'da, bir çözüm yolunun kalitesi, üzerinde biriktirilen feromon miktarıyla ilişkilendirilir. 
İyi bir çözüm yolundan geçen "sanal karıncalar" daha fazla feromon bırakır, böylece bu yolun gelecekte tercih edilme olasılığı artar.


2) Feromon Buharlaşması: 
Gerçek dünyada feromon izleri zamanla buharlaşır. 
Bu mekanizma, eski bilgilerin zamanla unutulmasını ve yeni çözümlerin keşfedilmesini sağlar. 
ACO'da da buharlaşma, algoritmanın yerel optimumlarda takılıp kalmamasına yardımcı olur.

3) Çözüm Yolu Oluşturma: Her bir karınca, çözüm uzayında rastgele veya önceki deneyimlere dayanarak bir yol oluşturur. 
Bu süreçte, karıncaların yolu seçme olasılığı, yol üzerindeki feromon miktarına bağlıdır.


4) Yerel ve Global Güncellemeler: 
Yol oluşturma sürecinin sonunda, geçilen yollar üzerindeki feromon miktarı güncellenir. 
Bu güncellemeler, yerel (yol oluşturma sırasında) ve global (en iyi çözüm bulunduktan sonra) olmak üzere iki seviyede gerçekleşir.



---- ACO'nun Uygulama Alanları ----
ACO, çeşitli optimizasyon problemlerinde kullanılabilir:

* Seyahat Eden Satıcı Problemi (TSP)
* Araç Rotalama Problemi (VRP)
* Zamanlama ve Planlama Problemleri
* Ağ Yönlendirme ve Bant Genişliği Tahsisi

'''

# karıncaların şehirler arasındaki en kısa yolu bulmasını amaçlayan bir seyahat satış temsilcisi problemi (TSP) için basit bir ACO uygulamasıdır.

import numpy as np

class AntColonyOptimizer:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        AntColonyOptimizer sınıfının başlatıcısı.
        distances: Şehirler arası mesafeleri içeren matris.
        n_ants: Kolonideki karınca sayısı.
        n_best: Her iterasyonda en iyi çözümleri seçmek için kullanılacak karınca sayısı.
        n_iterations: Algoritmanın çalıştırılacağı iterasyon sayısı.
        decay: Feromonun buharlaşma oranı.
        alpha: Feromon bilgisinin önem derecesi.
        beta: Uzaklık bilgisinin (heuristik bilgi) önem derecesi.
        """
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        best_cost = float('inf')
        for _ in range(self.n_iterations):
            all_paths = self.generate_all_paths()
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path, best_cost = self.find_shortest_path(all_paths, best_cost)
        return shortest_path, best_cost

    def generate_all_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.generate_path(0)  # Başlangıç şehri olarak 0'ı varsayalım.
            all_paths.append((path, self.path_cost(path)))
        return all_paths

    def generate_path(self, start):
        path = [start]
        visited = set(path)
        for _ in range(len(self.distances) - 1):
            move = self.select_next_city(path[-1], visited)
            path.append(move)
            visited.add(move)
        path.append(start)  # Başlangıç noktasına dönüş eklenir.
        return path

    def path_cost(self, path):
        return sum([self.distances[path[i], path[i+1]] for i in range(len(path)-1)])

    def spread_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, cost in sorted_paths[:n_best]:
            for move in range(len(path)-1):
                self.pheromone[path[move], path[move+1]] += 1.0 / self.distances[path[move], path[move+1]]
        self.pheromone *= self.decay  # Feromon buharlaşması

    def select_next_city(self, current, visited):
        probabilities = []
        for next_city in self.all_inds:
            if next_city not in visited:
                pheromone = self.pheromone[current][next_city] ** self.alpha
                heuristic = (1.0 / self.distances[current][next_city]) ** self.beta
                probabilities.append(pheromone * heuristic)
            else:
                probabilities.append(0)
        probabilities = probabilities / np.sum(probabilities)
        return np.random.choice(self.all_inds, 1, p=probabilities)[0]

    def find_shortest_path(self, all_paths, best_cost):
        shortest_path, shortest_path_cost = min(all_paths, key=lambda x: x[1])
        if shortest_path_cost < best_cost:
            return shortest_path, shortest_path_cost  # Yeni en iyi yol ve maliyeti döndür
        else:
            return shortest_path, best_cost  # Mevcut en iyi yolu koru (None döndürme)

    def run(self):
        shortest_path = None
        best_cost = float('inf')
        for _ in range(self.n_iterations):
            all_paths = self.generate_all_paths()
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)
            new_shortest_path, new_best_cost = self.find_shortest_path(all_paths, best_cost)
            if new_best_cost < best_cost:  # Yeni bir en iyi maliyet bulunduysa güncelle
                best_cost = new_best_cost
                shortest_path = new_shortest_path
        return shortest_path, best_cost


distances = np.array([
    [0, 1, 2, 3],  # 1. şehirden diğer şehirlere olan mesafeler
    [1, 0, 4, 5],  # 2. şehirden diğer şehirlere olan mesafeler
    [2, 4, 0, 6],  # 3. şehirden diğer şehirlere olan mesafeler
    [3, 5, 6, 0]   # 4. şehirden diğer şehirlere olan mesafeler
])
aco = AntColonyOptimizer(distances, n_ants=10, n_best=5, n_iterations=100, decay=0.5, alpha=1, beta=2)
path, cost = aco.run()
print("En kısa yol:", path)
print("Yolun maliyeti:", cost)


'''

Bu kodun çalışma prensibi şöyledir:

-- Başlangıç:

İlk olarak, şehirler arası mesafeler distances matrisi ile tanımlanır. 
Her yol için başlangıç feromon miktarı ayarlanır.



-- Yol Oluşturma: 
Her bir karınca için, generate_all_paths fonksiyonu kullanılarak başlangıç şehrinden başlayarak bir yol oluşturulur. 
generate_path fonksiyonu, ziyaret edilmemiş şehirlerden bir sonraki şehri seçmek için feromon miktarı ve şehirler arası mesafeye dayalı olasılıkları kullanır.



-- Feromon Yayılımı: 
Tüm karıncaların yolları oluşturulduktan sonra, spread_pheromone fonksiyonu ile her bir yol üzerindeki feromon miktarı güncellenir.
 En iyi yollar daha fazla feromon alır.

 

-- En İyi Yolun Bulunması: 
find_shortest_path fonksiyonu, tüm yollar arasından en düşük maliyete sahip olanı bulur ve bu en iyi yol olarak kaydedilir.



--İterasyon: 
Yukarıdaki adımlar, belirlenen iterasyon sayısı kadar tekrarlanır. 
Her iterasyon sonunda, en iyi yol güncellenir.



--Sonuç: 
Algoritma tamamlandığında, en kısa yol ve bu yolun maliyeti döndürülür.


'''