import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 20 * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")

        base_speed = random.uniform(20, 50)
        base_dir = pygame.Vector2(base_speed, 0).rotate(random.uniform(0, 360))

        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius / 2)

        asteroid1.velocity = base_dir.rotate(45) * 1.2
        asteroid2.velocity = base_dir.rotate(-45) * 1.2

        return [asteroid1, asteroid2]
