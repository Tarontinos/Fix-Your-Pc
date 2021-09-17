import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing

pygame.init()
pygame.display.set_caption(' ')
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
pygame.mouse.set_visible(False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()