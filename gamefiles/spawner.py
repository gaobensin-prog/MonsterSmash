from enemy import Enemy
import pygame
from gameobject import Gameobject
import random
from constants import screen_width,screen_length
from boss import Boss
class Spawner(Gameobject):
    def __init__(self):
        super().__init__()
        self.enemy = []
        self.boss = []
        self.boss_spawned = 0
        self.dt = 0
        self.dead = []
        self.wave = 0
    def update(self, dt, screen, wave):
        print(wave)
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_length)
        self.dt += dt 
        self.wave = wave
        if self.dt >= 1:
            enemy = Enemy(random_x, random_y)
            self.enemy.append(enemy)
            self.dt = 0
            if self.wave % 5 == 0 and self.boss_spawned == 0:
                self.boss_spawned += 1
                boss = Boss("boss")
                self.boss.append(boss)
            if self.wave % 3 == 0:
                self.boss_spawned = 0
    def draw(self, screen):
        for enemy in self.enemy:
            if enemy.health <= 0:
                self.dead.append(enemy)
                self.enemy.remove(enemy)
        for boss in self.boss:
            if boss.health <= 0:
                self.dead.append(boss)
                self.boss.remove(boss)
        for i in range(len(self.enemy)):
            self.enemy[i].draw(screen)
        for i in range(len(self.boss)):
            self.boss[i].draw(screen)

    def give_dead(self):
        dead = self.dead
        self.dead = []
        return dead
   