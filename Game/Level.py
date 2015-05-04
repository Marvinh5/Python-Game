__author__ = 'marvin'
import os
import fileinput
from Bricks.Brick import Brick
from Bricks.LifeBrick import LifeBrick
from Bricks.SpeedBrick import SpeedBrick
import pygame
from Shared.GameConstants import GameConstants


class Level:
    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__current_level = 0

    def get_bricks(self):
        return self.__bricks

    def get_amount_of_bricks_left(self):
        return self.__amountOfBricksLeft

    def get_current_level(self):
        return self.__amountOfBricksLeft

    def brick_hit(self, brick):
        self.__amountOfBricksLeft -= 1
        self.__bricks.remove(brick)

    def load_next_level(self):
        pass

    def load(self, level):
        self.__current_level = level
        self.__bricks = []
        x, y = 0, 0
        for line in fileinput.input(os.path.join("Assets", "Levels", "Level" + str(level))):
            for currentBrick in line:
                if currentBrick == "1":
                    brick = Brick((x, y), pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2":
                    brick = SpeedBrick((x, y), pygame.image.load(GameConstants.SPEED_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3":
                    brick = LifeBrick((x, y), pygame.image.load(GameConstants.LIFE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "4":
                    brick = SpeedBrick((x, y), pygame.image.load(GameConstants.SPEED_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE.get_width() + 1

            x = 0
            y += GameConstants.BRICK_SIZE.get_height() + 1

