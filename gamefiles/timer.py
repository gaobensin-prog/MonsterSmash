import pygame
from gameobject import Gameobject
class Timer(Gameobject):
    def __init__(self):
        super().__init__()
        self.time = 10
        self.rect = pygame.Rect(10, 5, 20, 10)
    def draw(self, screen, dt):
        if self.time > 0:
            self.time -= dt
            print(self.time)
        font = pygame.font.Font(None, 32)
        time = font.render(str(round(self.time)), False, "red")
        screen.blit(time, (self.rect.x, self.rect.y))