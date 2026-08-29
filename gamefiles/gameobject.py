import pygame
from constants import attack, health, defense
#Everything in the game will inherit from this class so that later it can be grouped into a container to be updated together
class Gameobject(pygame.sprite.Sprite):
    def __init__(self, hp: int = health, defs: int = defense, atk: int = attack) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
            self.__health = hp
            self.__defense = defs
            self.__attack = atk
    
    def get_stat(self, stat: str) -> int:
        if stat.lower() == "health":
            return self.__health
        elif stat.lower() == "defense":
            return self.__defense
        elif stat.lower() == "attack":
            return self.__attack
        else:
            raise ValueError("Please Enter a Valid Stat!")
    
    def update(self):
        raise ValueError("Each Class need its own Update() Method!")
    