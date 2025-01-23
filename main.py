import pygame
import pygame.display as display
import pygame.event as event_man
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    print("Starting asteroids!")
    screen = display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    player1=Player(c.SCREEN_WIDTH/2,c.SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while(True):
        for event in event_man.get():
            if event.type==pygame.QUIT:
                return
        for gameobject in updatable:
            gameobject.update(dt)
        
        screen.fill(color="black")
        for gameobject in drawable:
            gameobject.draw(screen)
        display.flip()
        dt=clock.tick(60)/1000

if __name__=="__main__":
    main()