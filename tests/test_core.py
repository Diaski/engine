import unittest
from engine.core import GameEngine

class TestGameEngine(unittest.TestCase):
    def test_initialization(self):
        game = GameEngine()
        self.assertTrue(game.is_running)

if __name__ == '__main__':
    unittest.main()
