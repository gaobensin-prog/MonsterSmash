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
        self.rect_hp = pygame.Rect(self.rect.center[0], self.rect.center[1], width_of_entity, height_of_entity)
        self.cooldown = 0
    def update(self):
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

    def attacking(self, enemy, dt):
        self.cooldown += dt
        if (
            self.rect.left * 2 <= enemy.rect.right
            and self.rect.right * 2 >= enemy.rect.left
            and self.rect.bottom * 2 >= enemy.rect.top
            and self.rect.top * 2 <= enemy.rect.bottom
            and self.cooldown >= 1
        ):
            enemy.change_stat(enemy.health, self.attack, enemy.defense)
            self.cooldown = 0