__author__ = 'marvin'


class GameObject(object):
    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__size = size
        self.__sprite = sprite

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_size(self):
        return self.__size

    def get_sprite(self):
        return self.__sprite

    def __x_collides(self, game_object):
        if (self.x + self.width) >= game_object.x and self.x + self.width <= (game_object.x + game_object.width):
            return True
        if game_object.x <= self.x <= game_object.x + game_object.width:
            return True
        return False

    def __y_collides(self, game_object):
        if (game_object.height + game_object.y) >= self.y <= (self.height + self.y) >= game_object.y:
            return True
        if game_object.y <= self.y <= game_object.y + game_object.height:
            return True
        return False

    def intersects(self, game_object):
        if self.__y_collides(game_object) and self.__x_collides(game_object):
            return True
        return False

