from gameobject import Gameobject
import pygame
class Wave(Gameobject):
    def __init__(self):
        super().__init__()
        self.time = 0

    def update(self, timer: object):
        self.time = timer.time
        if self.time <= 0:
            pygame.time.wait(5000)
            timer.time = 10