class Player:
    def __init__(self, position: tuple[float, float], size: tuple[int, int], color: tuple[int, int, int]):
        self.x, self.y = position
        
        self.width, self.height = size
        
        self.acc_y = 0.0
        self.vel_y = 0.0
        
        self.color = color

class Obstacle:
    vel_x = -65.0
    
    def __init__(self, position: tuple[float, float], size: tuple[int, int], color: tuple[int, int, int]):
        self.x, self.y = position
        
        self.width, self.height = size
        
        self.color = color