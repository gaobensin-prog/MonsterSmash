from gameobject import Gameobject
import pygame
from constants import screen_width
class Score(Gameobject):
    def __init__(self, dead_enemy = []):
        super().__init__()
        self.dead_enemy = dead_enemy
        self.score = 0
    
    def update(self, dead):
        self.dead_enemy = dead
    
    def draw(self, screen):
        self.score = len(self.dead_enemy)
        font = pygame.font.Font(None, 32)
        surface = font.render("Score = " + str(self.score), False, "red")
        screen.blit(surface, (1150, 0))
