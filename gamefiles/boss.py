from enemy import Enemy
import pygame
from getpictures import Picture
class Boss(Enemy):
    def __init__(self, boss):
        super().__init__(x = 1280 , y = 720 )
        self.boss = boss
        self.health = 1000
        self.attack = 100
        self.defense = 10
        self.rect = pygame.Rect(1280, 720, 200, 200)
        self.image = "niger.png"
        self.cooldown = 0
        
    def draw(self, screen):
        image = pygame.image.load(Picture(self.image).get_picture()).convert()
        sizew = 200 - image.get_width()
        sizeh = 200 - image.get_height()
        boss_img = pygame.transform.scale(image, (image.get_width() + sizew, image.get_height() + sizeh))
        screen.blit(boss_img, self.rect.topleft)
        self.healthbar(screen)

    def update(self, player, dt, screen):
        if self.health <= 0:
            self.kill()
            return
        if self.rect.centerx != player.rect.centerx:
            distance = player.rect.centerx - self.rect.centerx
            self.rect.centerx += distance * dt / 2
        if self.rect.centery != player.rect.centery:
            distance = player.rect.centery - self.rect.centery
            self.rect.centery += distance * dt / 2

    def healthbar(self, screen):
        health = pygame.font.Font(None, 40)
        surface = health.render(f"Niger {str(round(self.health))}", False, "red")
        screen.blit(surface, (self.rect.topleft))