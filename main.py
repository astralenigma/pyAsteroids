import sys
import pygame
import pygame.display as display
import pygame.event as event_man
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots,updatable,drawable)
    print("Starting asteroids!")
    screen = display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    player1=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while(True):
        for event in event_man.get():
            if event.type==pygame.QUIT:
                return
        for gameobject in updatable:
            gameobject.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    continue
            if asteroid.collides_with(player1):
                print("Game over!")
                sys.exit()
        screen.fill(color="black")
        for gameobject in drawable:
            gameobject.draw(screen)
        display.flip()
        dt=clock.tick(60)/1000

if __name__=="__main__":
    main()