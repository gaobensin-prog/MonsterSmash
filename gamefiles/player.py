from gameobject import Gameobject
import pygame
from getpictures import Picture
import sys
from constants import width_of_entity, height_of_entity
class Player(Gameobject):
    def __init__(self, screen, x: int  , y: int, image: str = "player.png") -> None:
        super().__init__()
        self.__picture = image
        self.health = 1000
        self.rect = pygame.Rect(x, y, width_of_entity, height_of_entity)
        self.rect_hp = pygame.Rect(0, 1280,  width_of_entity, height_of_entity)
    def update(self, enemy):
        keys = pygame.key.get_pressed()
        if self.health <= 0:
            self.kill()
            return
        if keys[pygame.K_a]:
            self.rect.x -= 10
            self.rect_hp.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
            self.rect_hp.x += 10
        if keys[pygame.K_s]:
            self.rect.y += 10
            self.rect_hp.y += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10
            self.rect_hp.y -= 10
        if (
            self.rect.x - width_of_entity / 2  <= enemy.rect.x + width_of_entity / 2
            and self.rect.x + width_of_entity / 2 >= enemy.rect.x - width_of_entity / 2
            and self.rect.y - height_of_entity / 2 <= enemy.rect.y + height_of_entity / 2
            and self.rect.y + height_of_entity / 2 >= enemy.rect.y - height_of_entity / 2
        ):
            self.change_stat(self.health, enemy.attack, self.defense)
        
    
    def draw(self, screen):
        pic = pygame.image.load(Picture(self.__picture).get_picture()).convert()
        sizew = width_of_entity - pic.get_width()
        sizeh = height_of_entity - pic.get_height()
        player_img = pygame.transform.scale(pic, (pic.get_width() + sizew, pic.get_height() + sizeh))
        screen.blit(player_img, self.rect)
        self.health_bar(screen)

    def get_stuff(self, stuff: str) -> tuple:
        if stuff.lower() == "image":
            return Picture(self.__picture).get_picture()
    
    def health_bar(self, screen):
        health = pygame.font.Font(None, 32)
        surface = health.render(str(round(self.health)), False, "red")
        screen.blit(surface, (self.rect_hp.x, self.rect_hp.y))