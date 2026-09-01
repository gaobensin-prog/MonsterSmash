from enemy import Enemy
from constants import screen_width,screen_length
import pygame
from gameobject import Gameobject
class Spawner(Gameobject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.list = []
        self.dt = 0
    def update(self, dt):
        self.dt += (dt * 10)
        if self.dt > 1:
            enemy = Enemy(screen_width / 2, screen_length / 2)
            self.list.append(enemy)
            self.dt = 0
    def draw(self, screen):
        for i in range(len(self.list)):
            self.list[i].draw(screen)