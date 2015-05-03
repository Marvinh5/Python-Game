__author__ = 'marvin'


class GameObject(object):
    def __init__(self, position, size, sprite):
        self.__position = position
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

    def get_sides(self):
        dimensions = []
        for x in range(self.__size.get_width()):
            dimensions.append({'x': self.get_position()[0], 'y': self.get_position()[0] + x})
        for x in range(self.__size.get_width()):
            dimensions.append({'x': self.get_position()[0]+self.__size.get_width(), 'y': x + self.get_position()[0]})

        return dimensions

    def x_collides(self, game_object):
        x1 = self.__position[0]
        x2 = game_object.get_position()[0]
        w1 = self.get_size().get_width()
        w2 = game_object.get_size().get_width()

        if x2 < x1 < x2 + w2:
            return True
        if x1 < x2 < x1 + w1:
            return True

        return False

    def y_collides(self, game_object):
        y1 = self.__position[1]
        y2 = game_object.get_position()[1]
        h1 = self.get_size().get_height()
        h2 = game_object.get_size().get_height()

        if y2 < y1 < y2 + h2:
            return True
        if y1 < y2 < y1 + h1:
            return True

        return False

    def intersects(self, game_object):
        if self.y_collides(game_object) and self.x_collides(game_object):
            return True
        return False

    def dimensions(self):
        dimensions = set([])

        x = self.get_position()[0]

        y = self.get_position()[1]

        width = self.get_size().get_width()

        height = self.get_size().get_height()

        for x_position in range(width):
            dimensions.add('{x},{y}'.format(x=x + x_position, y=y))
        for y_position in range(height):
            dimensions.add('{x},{y}'.format(x=x, y=y + y_position))
        for x_position in range(width):
            dimensions.add('{x},{y}'.format(x=x + x_position, y=y + height))
        for y_position in range(height):
            dimensions.add('{x},{y}'.format(x=x + width, y=y + y_position))

        return dimensions

    def collides_top(self, dimensions_of_objects):
        dimensions = set([])

        x = self.get_position()[0]

        y = self.get_position()[1]

        width = self.get_size().get_width()

        height = self.get_size().get_height()

        for x_position in range(width):
            dimensions.add('{x},{y}'.format(x=1 + x + x_position, y=y))

        return len(dimensions.intersection(dimensions_of_objects))


    def collides_right(self, dimensions_of_objects):
        dimensions = set([])

        x = self.get_position()[0]

        y = self.get_position()[1]

        width = self.get_size().get_width()

        height = self.get_size().get_height()

        for y_position in range(height):
            if y + y_position != y != y + height:
                dimensions.add('{x},{y}'.format(x=x + 1 + width, y=y + y_position))

        return len(dimensions.intersection(dimensions_of_objects))



    def collides_left(self, dimensions_of_objects):
        dimensions = set([])

        x = self.get_position()[0]

        y = self.get_position()[1]

        height = self.get_size().get_height()

        for y_position in range(height):
            if y + y_position != (y+1) != y + height:
                dimensions.add('{x},{y}'.format(x=x+1, y=y + y_position))

        return len(dimensions.intersection(dimensions_of_objects))


