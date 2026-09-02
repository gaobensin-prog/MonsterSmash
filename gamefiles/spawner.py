from enemy import Enemy
import pygame
from gameobject import Gameobject
import random
from constants import screen_width,screen_length
class Spawner(Gameobject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.list = []
        self.dt = 0
    def update(self, dt, screen):
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_length)
        self.dt += dt 
        if self.dt >= 1:
            enemy = Enemy(screen, random_x, random_y)
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