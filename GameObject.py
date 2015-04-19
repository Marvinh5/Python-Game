__author__ = 'marvin'


class GameObject(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def __x_collides(self, game_object):
        if (game_object.width + game_object.x) >= self.x <= (self.width + self.x) >= game_object.x:
            return True
        return False

    def __y_collides(self, game_object):
        if (game_object.height + game_object.y) >= self.y <= (self.height + self.y) >= game_object.y:
            return True
        return False

    def it_collides(self, game_object):
        if self.__y_collides(game_object) and self.__x_collides(game_object):
            return True
        return False

