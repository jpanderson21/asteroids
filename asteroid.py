import random
import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
                           pygame.Color("white"),
                           self.position,
                           self.radius,
                           width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        velocity_a = self.velocity.rotate(-angle)
        velocity_b = self.velocity.rotate(angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, radius)
        asteroid_a.velocity = velocity_a * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        asteroid_b = Asteroid(self.position.x, self.position.y, radius)
        asteroid_b.velocity = velocity_b * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
