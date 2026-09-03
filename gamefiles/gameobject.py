import pygame
from constants import attack, health, defense
#Everything in the game will inherit from this class so that later it can be grouped into a container to be updated together
class Gameobject(pygame.sprite.Sprite):
    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
    
    def update(self):
        raise ValueError("Each Class need its own Update() Method!")
    
    def change_stat(self, hp, atk, defs):
        new_hp = hp - (atk - defs)
        self.health = new_hp
    