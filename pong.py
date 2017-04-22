import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode( (640,480))

pygame.display.set_caption('Pygame Pong')

plaatje = pygame.image.load('test.jpg')
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	windowSurfaceObj.blit(plaatje, (0,0))
	pygame.display.update()
	fpsClock.tick(30)