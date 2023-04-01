import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PAINT")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (235, 35, 211)
def draw():
    l = 50
    for i in

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    pygame.display.flip()