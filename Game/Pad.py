__author__ = 'marvin'
from Shared import GameObject, GameConstants



class Pad(GameObject.GameObject):
    def __init__(self, position, sprite):
        super(Pad, self).__init__(position, GameConstants.GameConstants.PAD_SIZE, sprite)
    
    def move_right(self, x):
        if self.get_position()[0] + self.get_size().get_width() <= GameConstants.GameConstants.SCREEN_SIZE.get_size()[0]:   
            self.set_position((self.get_position()[0] + x, self.get_position()[1]))
    
    def move_left(self, x):
        if self.get_position()[0] - x > 0:
            self.set_position((self.get_position()[0] - x, self.get_position()[1]))