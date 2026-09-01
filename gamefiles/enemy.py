from gameobject import Gameobject
import random
from getpictures import Picture
from constants import screen_width,screen_length
import pygame
from spawner import Spawner
class Enemy(Gameobject):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.__position = pygame.Vector2(x, y)
        self.__image = "enemy.png"
    
    def update(self, player, dt):
        if self.health <= 0:
            self.kill()
            return
        if self.__position[0] != player.get_stuff("position")[0]:
            distance = player.get_stuff("position")[0] - self.__position[0]
            self.__position[0] += distance * dt
        if self.__position[1] != player.get_stuff("position")[1]:
            distance = player.get_stuff("position")[1] - self.__position[1]
            self.__position[1] += distance * dt
        if self.__position[0] < player.get_stuff("position")[0] and self.__position[1] < player.get_stuff("position")[1]:
            self.change_stat(self.health, player.atk, self.defense)
    
    def draw(self, screen: object):
        pic = pygame.image.load(Picture(self.__image).get_picture()).convert()
        enemy_img = pygame.transform.scale(pic, (pic.get_width() / 5, pic.get_height() / 5))
        screen.blit(enemy_img, self.__position)

    def get_stuff(self, stuff):
        if stuff.lower() == "position":
            return self.__position
        elif stuff.lower() == "image":
            return self.__image
    
    def delete_from_spawner(self, spawner):
        return
        del spawner.list[self]

