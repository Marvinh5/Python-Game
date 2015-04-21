__author__ = 'marvin'


class GameObject(object):
    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite
        print size, position

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_size(self):
        return self.__size

    def get_sprite(self):
        return self.__sprite

    def __x_collides(self, game_object):
        if (self.__position[0] + self.__size[0]) >= game_object.get_position[0] \
                and self.__position[0] + self.get_size[0] <= (game_object.get_position[0] + game_object.get_size[0]):
            return True
        if game_object.x <= self.__position[0] <= game_object.get_position[0] + game_object.width:
            return True
        return False

    def __y_collides(self, game_object):
        print game_object.get_position[0], game_object.get_size[0]
        if (game_object.get_size[1] + game_object.get_position[1]) >= self.get_position[1] <= (
                self.get_size[1] + self.get_position[1]) >= game_object.get_position[1]:
            return True
        if game_object.y <= self.get_position[1] <= game_object.y + game_object.get_size[1]:
            return True
        return False

    def intersects(self, game_object):
        if self.__y_collides(game_object) and self.__x_collides(game_object):
            return True
        return False

