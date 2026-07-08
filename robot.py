class Robot:
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y
        self.has_cargo = False
        
    def get_position(self):
        return (self.x, self.y)

    def move_up(self, warehouse_map):
        new_y = self.y - 1
        if new_y < 0:
            print("Error: Out of bounds (Top)!")
            return False
        if warehouse_map[new_y][self.x] == 1:
            print(f"Obstacle detected at ({self.x}, {new_y})! Recalculating...")
            return False
        
        self.y = new_y
        print(f"Moved UP. Current position: ({self.x}, {self.y})")
        return True

    def move_down(self, warehouse_map):
        new_y = self.y + 1
        max_y = len(warehouse_map)
        
        if new_y >= max_y:
            print("Error: Out of bounds (Bottom)!")
            return False
        if warehouse_map[new_y][self.x] == 1:
            print(f"Obstacle detected at ({self.x}, {new_y})! Recalculating...")
            return False
            
        self.y = new_y
        print(f"Moved DOWN. Current position: ({self.x}, {self.y})")
        return True

    def move_left(self, warehouse_map):
        new_x = self.x - 1
        
        if new_x < 0:
            print("Error: Out of bounds (Left)!")
            return False
        if warehouse_map[self.y][new_x] == 1:
            print(f"Obstacle detected at ({new_x}, {self.y})! Recalculating...")
            return False
            
        self.x = new_x
        print(f"Moved LEFT. Current position: ({self.x}, {self.y})")
        return True

    def move_right(self, warehouse_map):
        new_x = self.x + 1
        max_x = len(warehouse_map[0])
        
        if new_x >= max_x:
            print("Error: Out of bounds (Right)!")
            return False
        if warehouse_map[self.y][new_x] == 1:
            print(f"Obstacle detected at ({new_x}, {self.y})! Recalculating...")
            return False
            
        self.x = new_x
        print(f"Moved RIGHT. Current position: ({self.x}, {self.y})")
        return True