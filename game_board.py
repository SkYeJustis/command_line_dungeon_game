import logging
import os
import random
import sys

class GameBoard:

    def __init__(self, test_mode = False, dim = (3,3) ):
        self.GAME_DIMENSIONS = self.specify_game_dimensions(test_mode, dim)
        self.CELLS = self.build_cells()
        
    @staticmethod
    def clear():
        """Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def specify_game_dimensions(self, test_mode, dim):
        """Get game board dimension from user input"""
        self.clear()
        print("Please specify dungeon dimensions.")
        
        if test_mode == False:
            rows = input("How many rows would you like? ")
            columns = input("How many columns would you like? ")
            try:
                rows = int(rows)
            except:
                print("Please enter a number. Try again.")
                self.specify_game_dimensions()
            try:
                columns = int(columns)
            except:
                print("Please enter a number. Try again.")
                self.specify_game_dimensions()
        else:
            rows = dim[0]
            columns = dim[1]
        return (rows, columns)
        
    def build_cells(self):
        """Create and return a `width` x `height` grid of pairs
        """
        width, height = self.GAME_DIMENSIONS
        cells = []
        for y in range(height):
            for x in range(width):
                cells.append((x, y))
        return cells
        
    def get_locations(self):
        """Randomly pick starting locations for the monster, the door,
        and the player
        """
        monster = random.choice(self.CELLS)
        door = random.choice(self.CELLS)
        player = random.choice(self.CELLS)

        if monster == door or monster == player or door == player:
            monster, door, player = self.get_locations()
        
        return monster, door, player

    def get_moves(self, player_location):
        """Based on the tuple of the player's current position,
        return the list of acceptable moves
        """
        x, y = player_location
        moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
        if x == 0:
            moves.remove('LEFT')
        if x == self.GAME_DIMENSIONS[0] - 1:
            moves.remove('RIGHT')
        if y == 0:
            moves.remove('UP')
        if y == self.GAME_DIMENSIONS[1] - 1:
            moves.remove('DOWN')
        return moves
        
    def draw_map(self, player):
        print(' _'*self.GAME_DIMENSIONS[0])
        row_end = self.GAME_DIMENSIONS[0]
        tile = '|{}'
        for index, cell in enumerate(self.CELLS):
            if index % row_end < row_end - 1:
                if cell == player.location:
                    print(tile.format('X'), end='')
                elif cell in player.path:
                    print(tile.format('.'), end='')
                else:
                    print(tile.format('_'), end='')
            else:
                if cell == player.location:
                    print(tile.format('X|'))
                elif cell in player.path:
                    print(tile.format('.|'))
                else:
                    print(tile.format('_|'))
          
