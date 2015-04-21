import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class BreakOut:
    def __init__(self):
        self.__lives = 5
        self.__score = 0
        self.__level = Level(self)
        self.__level.load(0)
        self.__pad = Pad({0, 0}, 0)
        self.__balls = [
            Ball({0, 0},
                 pygame.image.load(GameConstants.GameConstants.SPRITE_BALL), self)]

        pygame.init()

        pygame.mixer.init()

        pygame.display.set_caption("Game Programing With Python")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__scenes = {
            0: PlayingGameScene(self),
            1: GameOverScene(self),
            2: HighScoreScene(self),
            3: MenuScene(self)
        }
        self.__currentScene = 0

        self.__sounds = {}

    def start(self):
        while 1:
            self.__clock.tick(100)

            self.screen.fill((0, 0, 0))

            current_scene = self.__scenes[self.__currentScene]

            current_scene.handle_events(pygame.event.get())

            current_scene.render()

            pygame.display.update()

    def change_scene(self, scene):
        self.__currentScene = scene

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score

    def increase_score(self, score):
        self.__score += score

    def get_lives(self):
        return self.__lives

    def get_balls(self):
        return self.__balls

    def get_pad(self):
        return self.__pad

    def play_sound(self, sound_clip):
        sound = self.__sounds[sound_clip]

        sound.stop()
        sound.play()

    def reduce_lives(self):
        self.__lives -= 1

    def increase_lives(self):
        self.__lives += 1

    def reset(self):
        pass


BreakOut().start()
