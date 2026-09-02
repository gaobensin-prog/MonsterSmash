from gameobject import Gameobject
import random
from getpictures import Picture
from constants import screen_width,screen_length
import pygame
class Enemy(Gameobject):
    def __init__(self, screen, x: int, y: int):
        super().__init__()
        self.__image = "enemy.png"
        self.rect = pygame.Rect(x, y, 300, 200)
    def update(self, player, dt, screen):
        if self.health <= 0:
            self.kill()
            return
        if self.rect.x != player.rect.x:
            distance = player.rect.x - self.rect.x
            self.rect.x += distance * dt
        if self.rect.y != player.rect.y:
            distance = player.rect.y - self.rect.y
            self.rect.y += distance * dt
        if self.rect.x < player.rect.x and self.rect.y < player.rect.y:
            self.change_stat(self.health, player.atk, self.defense)
    
    def draw(self, screen: object):
        pic = pygame.image.load(Picture(self.__image).get_picture()).convert()
        enemy_img = pygame.transform.scale(pic, (pic.get_width() / 5, pic.get_height() / 5))
        screen.blit(enemy_img, (self.rect.x, self.rect.y))
        

    def get_stuff(self, stuff):
        if stuff.lower() == "image":
            return self.__image

