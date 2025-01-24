import pygame
import random
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        angle=random.uniform(20,50)
        vector_angle1=self.velocity.rotate(angle)
        vector_angle2=self.velocity.rotate(-angle)
        ast1=Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        ast1.velocity=vector_angle1
        ast2=Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        ast2.velocity=vector_angle2