import pygame
from gameobject import Gameobject
from constants import wave_timer
class Timer(Gameobject):
    def __init__(self):
        super().__init__()
        self.time = 0
    def draw(self, screen, dt):
        if self.time > 0:
            self.time -= dt
        font = pygame.font.Font(None, 32)
        time = font.render(str(round(self.time)), False, "red")
        screen.blit(time, (10, 5))

    def reset_time(self, value = 10):
        
        self.time = 5
