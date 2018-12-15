import unittest

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
        
if __name__ == '__main__':
    unittest.main()
