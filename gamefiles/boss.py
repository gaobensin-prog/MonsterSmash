from enemy import Enemy
import pygame
from getpictures import Picture
class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 1000
        self.attack = 100
        self.defense = 10
        self.rect = pygame.Rect(1280, 720, 200, 200)
        self.image = "niger.png"
        self.cooldown = 0
    
    def draw(self, screen):
        image = pygame.image.load(Picture(self.image).get_picture()).convert()
        sizew = width_of_entity - pic.get_width()
        sizeh = height_of_entity - pic.get_height()
        boss_img = pygame.transform.scale(image, (image.get_width() + sizew, image.get_height() + sizeh))
        screen.blit(boss_img, self.rect.topleft)
        self.healthbar()