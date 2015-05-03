__author__ = 'marvin'
from Game.Shared import *


class Ball(GameObject.GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = False
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
        collides_top = False
        collides_left = False
        collides_right = False

        for x in objects:
            dimensions = x.dimensions()
            left_cordinates = self.collides_left(dimensions)
            right_cordinates = self.collides_right(dimensions)
            top_cordinates = self.collides_top(dimensions)

            if left_cordinates > right_cordinates and left_cordinates > top_cordinates:
                collides_left = True
            if right_cordinates > top_cordinates and right_cordinates > left_cordinates:
                collides_right = True
            if top_cordinates > left_cordinates and top_cordinates > right_cordinates:
                collides_top = True

        if collides_top:
            self.__direction[1] *= -1

        if collides_right or collides_left:
            self.__direction[0] *= -1




    def update_position(self):
        if self.__inMotion:
            if self.get_position()[1] >= GameConstants.SCREEN_SIZE.get_height() - GameConstants.BALL_SIZE.get_width() or \
                            self.get_position()[1] <= 0:
                self.__direction[1] *= -1

            if self.get_position()[0] >= GameConstants.SCREEN_SIZE.get_width() - GameConstants.BALL_SIZE.get_width() or \
                            self.get_position()[0] <= 0:
                self.__direction[0] *= -1

            y = self.get_position()[1] + (self.__speed * self.__direction[1])

            x = self.get_position()[0] + (self.__speed * self.__direction[0])

            self.set_position((x, y))

    def is_ball_dead(self):
        pass
