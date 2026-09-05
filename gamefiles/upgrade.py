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
            pygame.draw.rect(screen, "black", option, 3)
        font = pygame.font.Font(None, 32)
        count = 0
        for key in stats:
            for i in range(count,count + 1):
                x_center = self.option_list[i].centerx
                y_center = self.option_list[i].centery
                message = font.render(f"Current {key}: {str(stats[key])}", False, "red")
                screen.blit(message, (x_center - 100, y_center - 100))
                upgrade = font.render("Add 10", True, "green")
                screen.blit(upgrade, (x_center - 50, y_center + 100))
                count += 1
    
    def update(self, action, player):
        upgrade = ""
        if action.type == pygame.MOUSEBUTTONDOWN:
            location = action.pos
            for rect in self.option_list:
                if (
                    location[0] in range(rect.topleft[0],rect.topright[0]) and
                    location[1] in range(rect.topleft[1], rect.bottomright[1])
                ):
                    upgrade = rect
        if upgrade == self.option1:
            player.health += 10
            return True
        elif upgrade == self.option2:
            player.attack += 10
            return True
        elif upgrade == self.option3:
            player.defense += 10
            return True
