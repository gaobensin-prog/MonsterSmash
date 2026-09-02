from enemy import Enemy
import pygame
from gameobject import Gameobject
class Spawner(Gameobject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.list = []
        self.dt = 0
    def update(self, dt, screen):
        self.dt += dt 
        if self.dt >= 1:
            enemy = Enemy(screen)
            self.list.append(enemy)
            self.dt = 0
    def draw(self, screen):
        for enemy in self.list:
            if enemy.health <= 0:
                self.remove_from_list(enemy)
        for i in range(len(self.list)):
            self.list[i].draw(screen)
   
    def remove_from_list(self, enemy):
        self.list.remove(enemy)