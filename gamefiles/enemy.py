from gameobject import Gameobject
from getpictures import Picture
from constants import width_of_entity,height_of_entity,screen_width,screen_length,player_range
import pygame
import random
class Enemy(Gameobject):
    def __init__(self, screen, x: int = 0, y: int = 0):
        super().__init__()
        self.__image = "enemy.png"
        self.rect = pygame.Rect(x, y, width_of_entity, height_of_entity)
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
        if (
            self.rect.x - width_of_entity <= player.rect.x + width_of_entity / 2
            and self.rect.x + width_of_entity >= player.rect.x - width_of_entity / 2
            and self.rect.y - height_of_entity <= player.rect.y + height_of_entity / 2
            and self.rect.y + height_of_entity >= player.rect.y - height_of_entity / 2
        ):
            self.change_stat(self.health, player.attack, self.defense)
    
    def draw(self, screen: object):
        pic = pygame.image.load(Picture(self.__image).get_picture()).convert()
        sizew = width_of_entity - pic.get_width()
        sizeh = height_of_entity - pic.get_height()
        enemy_img = pygame.transform.scale(pic, (pic.get_width() + sizew * 1.15, pic.get_height() + sizeh * 1.15))
        screen.blit(enemy_img, (self.rect.x, self.rect.y))
        

    def get_stuff(self, stuff):
        if stuff.lower() == "image":
            return self.__image

