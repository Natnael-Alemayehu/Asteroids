import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        self.radius

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)

        movement_1 = self.velocity.rotate(split_angle)
        movement_2 = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_1.velocity = movement_1 * 1.2

        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2.velocity = movement_2 * 1.2
