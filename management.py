from robot import Robot

# 5x5'lik test depo haritamız
# Ortada dikey bir duvar (1) var, robotun etrafından dolanması gerekecek
test_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Robotu (0,2) yani sol orta noktada başlatalım
my_robot = Robot(start_x=0, start_y=2)

def draw_warehouse(warehouse_map, robot, path=None):
    """Depoyu, robotu ve eğer varsa planlanan ROTAYI (ASCII olararak) ekrana basar."""
    print("\n--- DEPO SİMÜLASYONU ---")
    for y in range(len(warehouse_map)):
        row_str = ""
        for x in range(len(warehouse_map[0])):
            # Eğer bu koordinatta robot varsa
            if x == robot.x and y == robot.y:
                row_str += "🤖 "
            # Eğer bu koordinat A* rotasının üzerindeyse '*' bas
            elif path and (x, y) in path:
                row_str += "* "
            # Eğer engel varsa '█' bas
            elif warehouse_map[y][x] == 1:
                row_str += "█ "
            # Boş yolsa '.' bas
            else:
                row_str += ". "
        print(row_str)
    print("-------------------------\n")

# 1. İlk durumu çizdir (Rota henüz yok)
print("Robot depoya giriş yaptı.")
draw_warehouse(test_map, my_robot)

# 2. Robota karşı tarafta bir hedef verelim (Örn: Duvarın hemen arkası (4,2))
target_coordinate = (4, 2)
print(f"Hedef Koordinat Belirlendi: {target_coordinate}")

# 3. Robotun A* algoritmasını tetikleyelim
calculated_path = my_robot.astar(test_map, target_coordinate)

# 4. Sonucu ekrana basalım
if calculated_path:
    print(f"A* Başarılı! Bulunan En Optimum Rota: {calculated_path}")
    # Harita üzerinde rotayı '*' işaretleriyle görelim
    draw_warehouse(test_map, my_robot, path=calculated_path)
else:
    print("Hata: Hedefe giden hiçbir yol bulunamadı!")