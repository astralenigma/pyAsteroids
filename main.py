import pygame
import pygame.display as display
import pygame.event as event_man
import constants as c
def main():
    print("Starting asteroids!")
    screen = display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    while(True):
        for event in event_man.get():
            if event.type==pygame.QUIT:
                return
        screen.fill(color="black")
        display.flip()
        dt=clock.tick(60)/1000

if __name__=="__main__":
    main()