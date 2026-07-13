class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        
    def __eq__(self, other):
        return self.position == other.position

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
            return False
        if warehouse_map[new_y][self.x] == 1:
            return False
        
        self.y = new_y
        return True

    def move_down(self, warehouse_map):
        new_y = self.y + 1
        max_y = len(warehouse_map)
        if new_y >= max_y:
            return False
        if warehouse_map[new_y][self.x] == 1:
            return False
            
        self.y = new_y
        return True

    def move_left(self, warehouse_map):
        new_x = self.x - 1
        if new_x < 0:
            return False
        if warehouse_map[self.y][new_x] == 1:
            return False
            
        self.x = new_x
        return True

    def move_right(self, warehouse_map):
        new_x = self.x + 1
        max_x = len(warehouse_map[0])
        if new_x >= max_x:
            return False
        if warehouse_map[self.y][new_x] == 1:
            return False
            
        self.x = new_x
        return True
    
    def astar(self, warehouse_map, target):
        start_node = Node(None, (self.x, self.y))
        target_node = Node(None, target)
        
        open_list = []
        closed_list = []
        open_list.append(start_node)
        
        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
                    
            open_list.pop(current_index)
            closed_list.append(current_node)
            
            if current_node == target_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
                
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[1] < 0 or node_position[1] >= len(warehouse_map) or \
                   node_position[0] < 0 or node_position[0] >= len(warehouse_map[0]):
                    continue
                    
                if warehouse_map[node_position[1]][node_position[0]] == 1:
                    continue
                    
                new_node = Node(current_node, node_position)
                children.append(new_node)
                
            for child in children:
                if child in closed_list:
                    continue
                    
                child.g = current_node.g + 1
                child.h = abs(child.position[0] - target_node.position[0]) + abs(child.position[1] - target_node.position[1])
                child.f = child.g + child.h
                
                skip = False
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        skip = True
                        break
                if skip:
                    continue
                        
                open_list.append(child)
                
        return None