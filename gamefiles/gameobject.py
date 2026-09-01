import pygame
from constants import attack, health, defense
#Everything in the game will inherit from this class so that later it can be grouped into a container to be updated together
class Gameobject(pygame.sprite.Sprite):
    def __init__(self, hp: int = health, defs: int = defense, atk: int = attack) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
            self.health = hp
            self.defense = defs
            self.attack = atk
        else:
            super().__init__()
            self.health = hp
            self.defense = defs
            self.attack = atk
    
    def update(self):
        raise ValueError("Each Class need its own Update() Method!")
    
    def change_stat(self, hp, atk, defs):
        new_hp = hp - (atk - defs)
        self.health = new_hp
    