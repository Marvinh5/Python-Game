__author__ = 'marvin'


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

    def brick_hit(self):
        self.__amountOfBricksLeft -= 1

    def load_next_level(self):
        pass

    def load(self):
        pass

