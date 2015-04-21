__author__ = 'marvin'
from Game.Bricks.Brick import Brick


class SpeedBrick(Brick):
    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)