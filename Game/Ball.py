__author__ = 'marvin'
from Shared.GameConstants import GameConstants
from Shared.GameObject import GameObject


class Ball(GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 1
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = False
        self.__hit_bottom = True
        position = (750, 550)
        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def speed(self, new_speed):
        self.__speed = new_speed

    def reset_speed(self):
        self.speed(3)

    def get_speed(self):
        return self.__speed

    def is_in_motion(self):
        return self.__inMotion

    def set_motion(self, is_moving):
        self.__inMotion = is_moving
        self.reset_speed()
    
    def change_direction(self, objects):
        for x in objects:
            if (self.collides_top(x) and (self.collides_left(x) or self.collides_right(x))) or self.collides_edges(x):
                self.__direction[0] *= -1
                self.__direction[1] *= -1
                return True
            if self.collides_top(x):
                self.__direction[1] *= -1
                return True
            if self.collides_right(x) or self.collides_left(x):
                self.__direction[0] *= -1
                return True

    def update_position(self):
        if self.__inMotion:
            if self.get_position()[1] >= GameConstants.SCREEN_SIZE.get_height() - GameConstants.BALL_SIZE.get_width() or \
                            self.get_position()[1] <= 0:
                self.__direction[1] *= -1
                self.__hit_bottom = True

            if self.get_position()[0] >= GameConstants.SCREEN_SIZE.get_width() - GameConstants.BALL_SIZE.get_width() or \
                            self.get_position()[0] <= 0:
                self.__direction[0] *= -1

            y = self.get_position()[1] + (self.__speed * self.__direction[1])

            x = self.get_position()[0] + (self.__speed * self.__direction[0])

            self.set_position((x, y))

    def is_ball_dead(self):
        pass
