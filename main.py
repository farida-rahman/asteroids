import pygame as pg
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pg.init()
	screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	clock = pg.time.Clock()
	dt = 0

	updateables = pg.sprite.Group()
	drawables = pg.sprite.Group()
	asteroids = pg.sprite.Group()
	shots = pg.sprite.Group()
	Player.containers = (updateables, drawables)
	Asteroid.containers = (asteroids, updateables, drawables)
	AsteroidField.containers = (updateables)
	Shot.containers = (shots, updateables, drawables)


	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)
	asteroidfield = AsteroidField()

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return

		screen.fill("black")
		for updateable in updateables:
			updateable.update(dt)
		
		for obj in asteroids:
			if obj.collision(player):
				print("Game Over!")
				sys.exit()
			else:
				continue

		for drawable in drawables:
			drawable.draw(screen)
		
		dt = clock.tick(60) / 1000
		pg.display.flip()

if __name__ == "__main__":
	main()
