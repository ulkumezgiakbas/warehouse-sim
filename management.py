import time
import random
from robot import Robot
from address import resolve_address
import settings

def generate_random_map(width, height, obstacle_probability, start_pos, target_pos):
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            if (x, y) == start_pos or (x, y) == target_pos:
                row.append(0)
            else:
                cell_value = 1 if random.random() < obstacle_probability else 0
                row.append(cell_value)
        grid.append(row)
    return grid

def draw_warehouse(warehouse_map, robot, path=None):
    print("\033[H\033[2J", end="")
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

target_x = random.randint(0, settings.WIDTH - 1)
target_y = random.randint(0, settings.HEIGHT - 1)

while target_x == settings.START_X and target_y == settings.START_Y:
    target_x = random.randint(0, settings.WIDTH - 1)
    target_y = random.randint(0, settings.HEIGHT - 1)

target_address = f"A-{target_x:02d}-{target_y:02d}"
target_coordinate = resolve_address(target_address)

if target_coordinate:
    test_map = generate_random_map(
        width=settings.WIDTH,
        height=settings.HEIGHT,
        obstacle_probability=settings.OBSTACLE_PROBABILITY,
        start_pos=(settings.START_X, settings.START_Y),
        target_pos=target_coordinate
    )

    my_robot = Robot(start_x=settings.START_X, start_y=settings.START_Y)
    
    draw_warehouse(test_map, my_robot)
    time.sleep(1.5)

    calculated_path = my_robot.astar(test_map, target_coordinate)

    if calculated_path:
        for step in calculated_path:
            my_robot.x = step[0]
            my_robot.y = step[1]
            draw_warehouse(test_map, my_robot, path=calculated_path)
            print(f"Target: {target_address} | Current Pos: ({my_robot.x}, {my_robot.y})")
            time.sleep(0.5)
            
        print("🎉 Mission accomplished! Product reached successfully.")
    else:
        draw_warehouse(test_map, my_robot)
        print("Error: No path found due to random obstacles blocking all ways!")
else:
    print("Error: Invalid address!")