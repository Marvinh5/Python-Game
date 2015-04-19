import pygame
import sys

pygame.init()

pygame.mixer.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = pygame.image.load("trujillo.jpg")
#myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

pygame.mouse.set_visible(0)

helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("shooting.wav")

x, y = 0, 0
directionX, directionY = 1, 1
clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                x += 5 if x >= 0 else 0
            if events.key == pygame.K_LEFT:
                x -= 5 if x >= 0 else 0

            if events.key == pygame.K_UP:
                y -= 5 if y >= 0 else 0
            if events.key == pygame.K_DOWN:
                y += 5 if y >= 0 else 0



    screen.fill((0, 0, 0))

    #mousePosition = pygame.mouse.get_pos()

   # x, y = mousePosition

    print(x, y)

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]
        sound.play()

    screen.blit(helloWorld, (x, y))

    pygame.display.update()