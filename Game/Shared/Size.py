__author__ = 'marvin'


class Size(object):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_size(self):
        return [self.__width, self.__height]