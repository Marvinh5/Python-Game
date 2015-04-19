import unittest
from GameObject import GameObject


class TestGame(unittest.TestCase):
    def test_y_collision(self):
        go = GameObject(3, 3, 1, 1)
        go2 = GameObject(3, 4, 1, 1)
        self.assertTrue(go.it_collides(go2) and go2.it_collides(go),
                        "Game object 1 should be colliding with Game object 2")

    def test_x_collision(self):
        go = GameObject(3, 3, 1, 1)
        go2 = GameObject(6, 3, 1, 1)
        self.assertFalse(go.it_collides(go2) and go2.it_collides(go),
                         "Game object 1 should not be colliding with Game object 2")

    def test_multiple_collision(self):
        go = GameObject(3, 3, 1, 1)
        go2 = GameObject(3.5, 3.5, 1, 1)
        self.assertTrue(go.it_collides(go2) and go2.it_collides(go),
                        "Game object 1 should collide with Game Object 2")

if __name__ == '__main__':
    unittest.main()
