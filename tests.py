import unittest

from game_board import GameBoard 
from player import Player


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.p1 = Player()
        
    def test_creation(self):
        self.assertIsNone(self.p1.location)
        self.assertEqual(self.p1.path, [])
    
    def test_move_left(self):
        self.p1.location = (2,2)
        self.p1.move_player('LEFT')
        self.assertEqual(self.p1.location, (1,2) )
    
    def test_move_right(self):
        self.p1.location = (2,2)
        self.p1.move_player('RIGHT')
        self.assertEqual(self.p1.location, (3,2) )
        
    def test_move_up(self):
        self.p1.location = (2,2)
        self.p1.move_player('UP')
        self.assertEqual(self.p1.location, (2,1) )
        
    def test_move_down(self):
        self.p1.location = (2,2)
        self.p1.move_player('DOWN')
        self.assertEqual(self.p1.location, (2,3) )

class GameBoardTests(unittest.TestCase):
    def setUp(self):
        self.gb1 = GameBoard(test_mode = True)
        self.gb2 = GameBoard(test_mode = True, dim = (5,5))
        
    def test_creation(self):
        self.assertEqual( self.gb1.GAME_DIMENSIONS, (3,3) )
        
    def test_specify_game_dimensions(self):
        self.assertEqual( self.gb2.GAME_DIMENSIONS, (5,5) )
        
    def test_build_cells(self):
        self.assertEqual( self.gb1.CELLS,
        [(0, 0), (1, 0), (2, 0), 
         (0, 1), (1, 1), (2, 1), 
         (0, 2), (1, 2), (2, 2),])
       
    def test_get_locations_values(self):
        monster, door, player = self.gb1.get_locations()
        test_result = True
        
        for cell in self.gb1.CELLS:
            if cell[0] < self.gb1.GAME_DIMENSIONS[0]:
                pass
            else:
                test_result = False
                print(self.gb1.GAME_DIMENSIONS)
                self.assertTrue(test_result)
                
            if cell[1] < self.gb1.GAME_DIMENSIONS[1]:
                pass
            else:
                test_result = False
                print(self.gb1.GAME_DIMENSIONS)
                self.assertTrue(test_result)
                
        self.assertTrue(test_result)
        
    def test_get_locations_type(self):
        monster, door, player = self.gb1.get_locations()
        self.assertIsInstance(monster, type((0,0)) )
        self.assertIsInstance(door, type((0,0)) )
        self.assertIsInstance(player, type((0,0)) )
        
    def test_get_moves(self):
        self.assertEquals([ 'RIGHT', 'UP', 'DOWN'], 
                        self.gb1.get_moves((0,1)))
        self.assertEquals(['LEFT', 'UP', 'DOWN'], 
                        self.gb1.get_moves((3-1,1)))
        self.assertEquals(['LEFT', 'RIGHT', 'DOWN'], 
                        self.gb1.get_moves((1,0)))
        self.assertEquals(['LEFT', 'RIGHT', 'UP'],
                        self.gb1.get_moves((1,3-1)))
       
       
if __name__ == '__main__':
    unittest.main()
