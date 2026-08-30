from gameobject import Gameobject
import random
from getpictures import Picture
from constants import screen_width,screen_length
import pygame
class Enemy(Gameobject):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.__position = pygame.Vector2(x, y)
        self.__image = "enemy.png"
    
    def update(self, player):
        if self.__position[0] != player.get_stuff("position")[0]:
            self.__position[0] += 1
            self.__position[1] += 1

    def draw(self, screen: object):
        pic = pygame.image.load(Picture(self.__image).get_picture()).convert()
        enemy_img = pygame.transform.scale(pic, (pic.get_width() / 5, pic.get_height() / 5))
        screen.blit(enemy_img, self.__position)

