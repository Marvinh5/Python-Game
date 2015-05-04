__author__ = 'marvin'

from Brick import Brick


class LifeBrick(Brick):
    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)