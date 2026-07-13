import time
from robot import Robot
from address import resolve_address

test_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

my_robot = Robot(start_x=0, start_y=2)

def draw_warehouse(warehouse_map, robot, path=None):
    print("\n--- DEPO DURUMU ---")
    for y in range(len(warehouse_map)):
        row_str = ""
        for x in range(len(warehouse_map[0])):
            if x == robot.x and y == robot.y:
                row_str += "🤖 "
            elif path and (x, y) in path:
                row_str += "* "
            elif warehouse_map[y][x] == 1:
                row_str += "█ "
            else:
                row_str += ". "
        print(row_str)
    print("-------------------\n")

print("Robot depoya giriş yaptı.")
draw_warehouse(test_map, my_robot)

target_address = "A-04-02" 
print(f"Gelen Sipariş Adresi: {target_address}")

target_coordinate = resolve_address(target_address)

if target_coordinate:
    print(f"Adres Başarıyla Çözümlendi -> Koordinat: {target_coordinate}")
    calculated_path = my_robot.astar(test_map, target_coordinate)

    if calculated_path:
        print(f"En Optimum Rota Hesaplandı: {calculated_path}")
        draw_warehouse(test_map, my_robot, path=calculated_path)
    else:
        print("Hata: Hedef adrese giden bir yol bulunamadı!")
else:
    print("Hata: Geçersiz adres nedeniyle işlem iptal edildi.")