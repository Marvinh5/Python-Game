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
    
    def get_borders(self):
        x = self.get_position()[0]
        y = self.get_position()[1]
        top_left     = (x, y)
        top_right    = (x + self.get_size().get_width(), y)
        bottom_left  = (x, y + self.get_size().get_height())
        bottom_right = (x + self.get_size().get_width(), y + self.get_size().get_height())
        return ('', top_left, top_right, bottom_left, bottom_right)
    
    def collides_edges(self, game_object):
        borders = self.get_borders()
        borders2 = game_object.get_borders()
        if borders2[4][0] >= borders[1][0] and borders[1][0] >= borders[1][0]:
            if abs(borders[1][0] - borders2[1][0]) > abs(borders[1][1] - borders[1][1]):
                return True,'Top'
            else:
                return True, 'Sides'
            return False,''
        return False,''
    
    def x_collides(self, game_object):
        x1 = self.__position[0]
        x2 = game_object.get_position()[0]
        w1 = self.get_size().get_width()
        w2 = game_object.get_size().get_width()
        
        if x2 + w2 >= x1 and x2 + w2 <= x1 + w1:
            return True
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
        
        if y2 + h2 >= y1 and y2 + h2 <= y1 + h1:
            return True
        
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
    
    
    def collides_top(self, game_object):
        max_x = game_object.get_position()[0] + game_object.get_size().get_width()
        min_x = game_object.get_position()[0]
        
        
        if(min_x <= (self.get_position()[0] + self.get_size().get_width()/2) <= max_x):
            if(game_object.get_position()[1] <= self.get_position()[1]  <= game_object.get_position()[1] + game_object.get_size().get_height()):
                return True
            return False
        return False
    
    def collides_bottom(self, game_object):
        max_x = game_object.get_position()[0] + game_object.get_size().get_width()
        min_x = game_object.get_position()[0]
        
        max_y = game_object.get_position()[1] + game_object.get_size().get_height()
        min_y = game_object.get_position()[1]
        
        if(min_x <= self.get_position()[0] <= max_x):
            if min_y <= self.get_position()[1]  <= max_y:
                return True
        return False


    def collides_right(self, game_object):
        max_y = game_object.get_position()[1] + game_object.get_size().get_height()
        min_y = game_object.get_position()[1]
        
        if(min_y <= (self.get_position()[1] + self.get_size().get_height()/2) <= max_y):
            if(game_object.get_position()[0] <= self.get_position()[0] <= game_object.get_position()[0]+game_object.get_size().get_width()):
                return True
            return False
        return False


    def collides_left(self, game_object):
        max_x = game_object.get_position()[1] + game_object.get_size().get_height()
        min_x = game_object.get_position()[1]
        
        if(min_x <= (self.get_position()[1] + self.get_size().get_height()/2) <= max_x):
            if(game_object.get_position()[0] <= self.get_position()[0] <= game_object.get_position()[0]+game_object.get_size().get_width()):
                return True
            return False
        return False


