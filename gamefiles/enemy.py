from gameobject import Gameobject
from getpictures import Picture
from constants import width_of_entity,height_of_entity,screen_width,screen_length,player_range
import pygame
import random
class Enemy(Gameobject):
    def __init__(self, screen, x: int = -1000, y: int = -1000):
        super().__init__()
        self.__image = "enemy.png"
        self.rect = pygame.Rect(x, y, width_of_entity, height_of_entity)
        self.rect_hp = pygame.Rect(self.rect.centerx, self.rect.centery, width_of_entity, height_of_entity)
        self.cooldown = 0
    def update(self, player, dt, screen):
        if self.health <= 0:
            self.kill()
            return
        if self.rect.x != player.rect.x:
            distance = player.rect.x - self.rect.x
            self.rect.x += distance * dt
            self.rect_hp.x += distance * dt
        if self.rect.y != player.rect.y:
            distance = player.rect.y - self.rect.y
            self.rect.y += distance * dt
            self.rect_hp.y += distance * dt
    
    def draw(self, screen: object):
        pic = pygame.image.load(Picture(self.__image).get_picture()).convert()
        sizew = width_of_entity - pic.get_width()
        sizeh = height_of_entity - pic.get_height()
        enemy_img = pygame.transform.scale(pic, (pic.get_width() + sizew * 1.15, pic.get_height() + sizeh * 1.15))
        screen.blit(enemy_img, (self.rect.x, self.rect.y))
        self.healthbar(screen)
        

    def get_stuff(self, stuff):
        if stuff.lower() == "image":
            return self.__image

    def attacking(self, player, dt):
        self.cooldown += dt
        if (
            self.rect.left <= player.rect.right
            and self.rect.right >= player.rect.left
            and self.rect.bottom >= player.rect.top
            and self.rect.top <= player.rect.bottom
            and self.cooldown >= 1
        ):
            player.change_stat(player.health, self.attack, player.defense)
            self.cooldown = 0

    def healthbar(self, screen):
        health = pygame.font.Font(None, 20)
        surface = health.render(str(round(self.health)), False, "red")
        screen.blit(surface, (self.rect_hp.x, self.rect_hp.y))