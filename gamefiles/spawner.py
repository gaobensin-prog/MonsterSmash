from enemy import Enemy
from constants import screen_width,screen_length
import pygame
from gameobject import Gameobject
class Spawner(Gameobject):
    def __init__(self, screen):
        super().__init__()
        self.__screen = screen
        self.__list = []
        self.__dt = 0
    def update(self, dt):
        self.__dt += (dt / 10)
        if self.__dt > 1:
            enemy = Enemy(screen_width / 2, screen_length / 2)
            self.__list.append(enemy)
            self.__dt = 0
    def draw(self, screen):
        for i in range(len(self.__list)):
            self.__list[i].draw(screen)