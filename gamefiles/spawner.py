from enemy import Enemy
import pygame
from gameobject import Gameobject
import random
from constants import screen_width,screen_length
class Spawner(Gameobject):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.enemy = []
        self.dt = 0
        self.dead = []
    def update(self, dt, screen):
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_length)
        self.dt += dt 
        if self.dt >= 1:
            enemy = Enemy(screen, random_x, random_y)
            self.enemy.append(enemy)
            self.dt = 0
    def draw(self, screen):
        for enemy in self.enemy:
            if enemy.health <= 0:
                self.dead.append(enemy)
                self.enemy.remove(enemy)
        for i in range(len(self.enemy)):
            self.enemy[i].draw(screen)
   