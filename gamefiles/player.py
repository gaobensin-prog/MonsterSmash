from gameobject import Gameobject
import pygame
from getpictures import Picture
import sys
class Player(Gameobject):
    def __init__(self, x: int  , y: int, image: str = "player.png") -> None:
        super().__init__()
        self.__position = pygame.Vector2(x,y) 
        self.__picture = image
        self.atk = 1000
        self.health = 1000
    def update(self, enemy):
        keys = pygame.key.get_pressed()
        if self.health <= 0:
            self.kill()
            return
        if keys[pygame.K_a]:
            self.__position[0] -= 10
        if keys[pygame.K_d]:
            self.__position[0] += 10
        if keys[pygame.K_s]:
            self.__position[1] += 10
        if keys[pygame.K_w]:
            self.__position[1] -= 10
        if self.__position[0] < enemy.get_stuff("position")[0] and self.__position[1] < enemy.get_stuff("position")[1]:
            print(self.health)
            self.change_stat(self.health, enemy.attack, self.defense)
        
    
    def draw(self, screen):
        pi = pygame.image.load(Picture(self.__picture).get_picture()).convert()
        player_img = pygame.transform.scale(pi, (pi.get_width() / 5, pi.get_height() / 5))
        screen.blit(player_img, self.__position)

    def get_stuff(self, stuff: str) -> tuple:
        if stuff.lower() == "position":
            return self.__position
        elif stuff.lower() == "image":
            return Picture(self.__picture).get_picture()