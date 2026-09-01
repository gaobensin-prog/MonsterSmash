from gameobject import Gameobject
import pygame
from getpictures import Picture
class Player(Gameobject):
    def __init__(self, x: int = 1280/2 , y: int = 720/2, image: str = "player.png") -> None:
        super().__init__()
        self.__position = pygame.Vector2(x,y) 
        self.__picture = image
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.__position[0] -= 10
        if keys[pygame.K_d]:
            self.__position[0] += 10
        if keys[pygame.K_s]:
            self.__position[1] += 10
        if keys[pygame.K_w]:
            self.__position[1] -= 10
    
    def draw(self, screen):
        pi = pygame.image.load(Picture(self.__picture).get_picture()).convert()
        player_img = pygame.transform.scale(pi, (pi.get_width() / 5, pi.get_height() / 5))
        screen.blit(player_img, self.__position)

    def get_stuff(self, stuff: str) -> tuple:
        if stuff.lower() == "position":
            return self.__position
        elif stuff.lower() == "image":
            return Picture(self.__picture).get_picture()
    
