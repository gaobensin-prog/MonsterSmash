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
    def update(self, enemy):
        keys = pygame.key.get_pressed()
        if self.health <= 0:
            self.kill()
            return
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if (
            self.rect.x - width_of_entity / 2  <= enemy.rect.x + width_of_entity / 2
            and self.rect.x + width_of_entity / 2 >= enemy.rect.x - width_of_entity / 2
            and self.rect.y - height_of_entity / 2 <= enemy.rect.y + height_of_entity / 2
            and self.rect.y + height_of_entity / 2 >= enemy.rect.y - height_of_entity / 2
        ):
            print(self.health)
            self.change_stat(self.health, enemy.attack, self.defense)
        
    
    def draw(self, screen):
        pi = pygame.image.load(Picture(self.__picture).get_picture()).convert()
        player_img = pygame.transform.scale(pi, (pi.get_width() / 5, pi.get_height() / 5))
        screen.blit(player_img, self.rect)

    def get_stuff(self, stuff: str) -> tuple:
        if stuff.lower() == "image":
            return Picture(self.__picture).get_picture()