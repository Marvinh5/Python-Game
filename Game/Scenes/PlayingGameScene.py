from Scene import Scene

__author__ = 'marvin'

import pygame


class PlayingGameScene(Scene):
    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handle_events(self, events):
        super(PlayingGameScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def manage_ball_collision(self, game):
        elements_intersected = []
        for ball in game.get_balls():
            for current_brick in game.get_level().get_bricks():
                if current_brick.intersects(ball):
                    elements_intersected.append(current_brick)
            if len(elements_intersected) > 0:
                ball.change_direction(elements_intersected)
                for brick in elements_intersected:
                    game.get_level().brick_hit(brick)
                elements_intersected = []
            
            ball.update_position()
            
            game.screen.blit(ball.get_sprite(), ball.get_position())

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.get_game()

        self.manage_ball_collision(game)

        for brick in game.get_level().get_bricks():
            if not brick.is_destroyed():
                game.screen.blit(brick.get_sprite(), brick.get_position())