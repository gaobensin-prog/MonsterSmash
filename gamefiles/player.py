from gameobject import Gameobject
import pygame
from getpictures import Picture
class Player(Gameobject):
    def __init__(self, x: int, y: int, image: str = "player.png") -> None:
        super().__init__()
        self.position = pygame.Vector2(x,y) 
        self.picture = image
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position[0] -= 10
        if keys[pygame.K_d]:
            self.position[0] += 10
        if keys[pygame.K_s]:
            self.position[1] += 10
        if keys[pygame.K_w]:
            self.position[1] -= 10
    
    def draw(self, screen):
        player_img = pygame.image.load(Picture(self.picture).get_picture()).convert()
        screen.blit(player_img, self.position)

