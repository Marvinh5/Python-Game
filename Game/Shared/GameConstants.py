__author__ = 'marvin'
import os
from Size import Size


class GameConstants:
    SCREEN_SIZE = Size(width=800, height=600)
    BRICK_SIZE = Size(width=100, height=30)
    BALL_SIZE = Size(width=32, height=32)
    PAD_SIZE = Size(width=139, height=13)

    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "brick.png")
    LIFE_BRICK = os.path.join("Assets", "LifeBrick.png")
    SPEED_BRICK = os.path.join("Assets", "SuperBrickNormal.png")
    SPRITE_PAD = os.path.join("Assets", "pad.png")
    SOUND_BRICK_HIT = os.path.join("Assets", "metal_hit.mp3")
    SOUND_GAME_OVER = os.path.join("Assets", "game_over.wav")
    

    def __init__(self):
        pass