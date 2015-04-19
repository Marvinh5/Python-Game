import unittest
from GameObject import GameObject


class TestGame(unittest.TestCase):
    def test_y_collision(self):
        go = GameObject(3, 3, 1, 1)

        go2 = GameObject(3, 4, 1, 1)

        go3 = GameObject(3, 5, 1, 1)

        go4 = GameObject(3, 1, 1, 1)

        go5 = GameObject(3, 2, 1, 1)

        go6 = GameObject(3, 3.5, 1, 1)

        self.assertTrue(go.collides_with(go2) and go2.collides_with(go),
                        "Game object 1 should be colliding with Game object 2")

        self.assertFalse(go.collides_with(go3) and go3.collides_with(go),
                         "Game object 1 should not be colliding with Game object 3")

        self.assertFalse(go.collides_with(go4) and go4.collides_with(go),
                         "Game object 1 should not be colliding with Game object 4")

        self.assertTrue(go.collides_with(go5) and go5.collides_with(go),
                        "Game object 1 should be colliding with Game object 5")

        self.assertTrue(go.collides_with(go6) and go6.collides_with(go),
                        "Game object 1 should be colliding with Game object 6")

    def test_x_collision(self):
        go = GameObject(3, 3, 1, 1)

        go2 = GameObject(6, 3, 1, 1)

        self.assertFalse(go.collides_with(go2) and go2.collides_with(go),
                         "Game object 1 should not be colliding with Game object 2")

    def test_multiple_collision(self):
        go = GameObject(3, 3, 1, 1)
        go2 = GameObject(3.5, 3.5, 1, 1)

        go3 = GameObject(1.5, 3.5, 1, 1)

        go4 = GameObject(6, 3, 1, 1)

        self.assertTrue(go.collides_with(go2) and go2.collides_with(go),
                        "Game object 1 should collide with Game Object 2")

        self.assertFalse(go3.collides_with(go) and go.collides_with(go3),
                         "Game object 1 should not collide with Game Object 3")

        self.assertFalse(go4.collides_with(go) and go.collides_with(go4),
                         "Game object 1 should not collide with Game Object 4")


if __name__ == '__main__':
    unittest.main()
