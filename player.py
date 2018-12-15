
class Player:
    
    location = None
    path = []
    
    def __init__(self, location = None):
        self.location = location
        
    def move_player(self, move):
        x, y = self.location
        self.path.append((x, y))
        if move == 'LEFT':
            x -= 1
        elif move == 'UP':
            y -= 1
        elif move == 'RIGHT':
            x += 1
        elif move == 'DOWN':
            y += 1
        self.location = (x, y)
        return x, y
    
