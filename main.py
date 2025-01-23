import pygame
import pygame.display as display
import pygame.event as event_man
import constants as c
import player
def main():
    print("Starting asteroids!")
    screen = display.set_mode((c.SCREEN_WIDTH,c.SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    player1=player.Player(c.SCREEN_WIDTH/2,c.SCREEN_HEIGHT/2)
    while(True):
        for event in event_man.get():
            if event.type==pygame.QUIT:
                return
        screen.fill(color="black")
        player1.draw(screen)
        display.flip()
        dt=clock.tick(60)/1000

if __name__=="__main__":
    main()