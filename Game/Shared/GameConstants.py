__author__ = 'marvin'
import os


class GameConstants:
    SCREEN_SIZE = [800, 600]
    BRICK_SIZE = (100, 30)
    BALL_SIZE = [60, 60]
    PAD_SIZE = [139, 13]

    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "NormalBrick.png")
    LIFE_BRICK = os.path.join("Assets", "LifeBrick.png")
    SPEED_BRICK = os.path.join("Assets", "SuperBrickNormal.png")

    def __init__(self):
        pass

