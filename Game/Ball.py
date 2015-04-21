__author__ = 'marvin'
from Game.Shared import *
import pygame


class Ball(GameObject.GameObject):
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 3
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = False

        super(Ball, self).__init__(position, GameConstants.GameConstants.BALL_SIZE, sprite)

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

    def change_direction(self, game_object):
        pass

    def update_position(self):
        self.set_position(pygame.mouse.get_pos())

    def is_ball_dead(self):
        pass
