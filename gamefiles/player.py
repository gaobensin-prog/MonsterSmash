from gameobject import Gameobject
import pygame
from getpictures import Picture
import sys
from constants import width_of_entity, height_of_entity
class Player(Gameobject):
    def __init__(self, x: int  , y: int, image: str = "player.png") -> None:
        super().__init__()
        self.__picture = image
        self.health = 1000
        self.rect = pygame.Rect(x, y, width_of_entity, height_of_entity)
        self.cooldown = 0
        self.attack = 10
        self.defense = 2.5
    def update(self):
        keys = pygame.key.get_pressed()
        if self.health <= 0:
            self.kill()
            return
        if keys[pygame.K_a]:
            self.rect.centerx -= 10
        if keys[pygame.K_d]:
            self.rect.centerx += 10
        if keys[pygame.K_s]:
            self.rect.centery += 10
        if keys[pygame.K_w]:
            self.rect.centery -= 10
    
    def draw(self, screen):
        pic = pygame.image.load(Picture(self.__picture).get_picture()).convert()
        sizew = width_of_entity - pic.get_width()
        sizeh = height_of_entity - pic.get_height()
        player_img = pygame.transform.scale(pic, (pic.get_width() + sizew, pic.get_height() + sizeh))
        screen.blit(player_img, (self.rect.topleft))
        self.health_bar(screen)

    def get_stuff(self, stuff: str) -> tuple:
        if stuff.lower() == "image":
            return Picture(self.__picture).get_picture()
    
    def health_bar(self, screen):
        health = pygame.font.Font(None, 32)
        surface = health.render(str(round(self.health)), False, "red")
        screen.blit(surface, (self.rect.topleft))

    def attacking(self, enemy, dt):
        if (
            self.rect.left <= enemy.rect.right
            and self.rect.right  >= enemy.rect.left 
            and self.rect.bottom  >= enemy.rect.top 
            and self.rect.top  <= enemy.rect.bottom
        ):
            enemy.change_stat(enemy.health, self.attack, enemy.defense)

    def return_stats(self):
        return {"Health": self.health, "Attack": self.attack, "Defense": self.defense}