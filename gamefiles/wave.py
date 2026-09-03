from gameobject import Gameobject
import pygame
class Wave(Gameobject):
    def __init__(self,time):
        super().__init__()
        self.time = time

    def update(self, time):
        self.time = time.time
        if self.time <= 0:
            pygame.time.delay(5000)