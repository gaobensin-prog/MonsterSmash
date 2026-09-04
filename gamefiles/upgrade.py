from gameobject import Gameobject
import pygame
class Upgrade(Gameobject):
    def __init__(self):
        super().__init__()
        self.option1 = pygame.Rect(100, 100, 300, 400)
        self.option2 = pygame.Rect(500, 100, 300, 400)
        self.option3 = pygame.Rect(900, 100, 300, 400)
        self.option_list = [self.option1, self.option2, self.option3]
    def draw(self, screen, stats):
        for option in self.option_list:
            pygame.draw.rect(screen, "black", option, 1)
        font = pygame.font.Font(None, 32)
        count = 0
        for key in stats:
            for i in range(count,count + 1):
                message = font.render(f"Current {key} is: {str(stats[key])}", False, "red")
                screen.blit(message, (self.option_list[i].centerx - 100, self.option_list[i].centery - 100))
                count += 1