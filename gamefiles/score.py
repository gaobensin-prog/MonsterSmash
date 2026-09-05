from gameobject import Gameobject
import pygame
from constants import screen_width
from boss import Boss
class Score(Gameobject):
    def __init__(self):
        super().__init__()
        self.dead_enemy = []
        self.score = 0
    
    def update(self, dead):
        if dead != []:
            self.dead_enemy = dead
        for enemy in self.dead_enemy:
            if isinstance(enemy, Boss):
                self.score += 100
            else:
                self.score += 1
        self.dead_enemy = []
    def draw(self, screen):
        font = pygame.font.Font(None, 32)
        surface = font.render("Score = " + str(self.score), False, "red")
        screen.blit(surface, (1150, 0))
