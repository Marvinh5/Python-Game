__author__ = 'marvin'
from Shared import GameObject, GameConstants



class Pad(GameObject.GameObject):
    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.GameConstants.PAD_SIZE, sprite)