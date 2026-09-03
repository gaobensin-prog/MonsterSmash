from gameobject import Gameobject
import pygame
from constants import screen_width
class Score(Gameobject):
    def __init__(self, dead_enemy):
        self.dead_enemy = dead_enemy
        self.score = 0
        self.rect = pygame.Rect(1000, screen_width, 50, 50)
    
    def draw(self, screen):
        self.score = len(self.dead_enemy)
        self.dead_enemy = []
        font = pygame.font.Font(None, 32)
        surface = font.render(str(self.score), False, "red")
        screen.blit(surface, (self.rect.x,self.rect.y))
