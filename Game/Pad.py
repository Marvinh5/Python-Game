__author__ = 'marvin'
from Game.Shared import *


class Pad(GameObject.GameObject):
    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.PAD_SIZE, sprite)