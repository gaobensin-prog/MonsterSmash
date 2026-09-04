from gameobject import Gameobject
import pygame
class Wave(Gameobject):
    def __init__(self):
        super().__init__()
        self.upgrade_time = 0
    def update(self, dt, time):
        if time <= 0 :
            self.upgrade_time += dt
            if self.upgrade_time >= 10:
                self.upgrade_time = 0
                return "playing"
            return "upgrading"
        return "playing"
        