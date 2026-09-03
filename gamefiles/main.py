import pygame
from constants import screen_width, screen_length
from player import Player
from enemy import Enemy
from spawner import Spawner
import random
from timer import Timer
from score import Score
from wave import Wave
def main():
    #just like git init we make the game file
    pygame.init()
    #make the screen
    screen = pygame.display.set_mode((screen_width, screen_length))
    #clock system to limit the frame at which the game can run
    clock = pygame.time.Clock()
    dt = 0
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    attackable = pygame.sprite.Group()
    Enemy.containers = (updatable, drawable, attackable)
    enemy = Enemy(screen)
    Player.containers = (updatable, drawable, attackable)
    player = Player(screen, 50, 50)
    Spawner.containers = (updatable, drawable)
    spawner = Spawner(screen)
    Timer.containers = (drawable,)
    timer = Timer()
    Score.containers = (drawable, updatable)
    score = Score()
    Wave.containers = (updatable,)
    wave = Wave()
    running = True
    game_state = "playing"
    while running:
        screen.fill("white")
        #check what the player is clicking on in the game
        for event in pygame.event.get():
            #check if the player click the X button
            if event.type == pygame.QUIT:
                #if so turn the running to False so the while loop can stop
                running = False
            if player not in updatable:
                running = False
        if game_state == "playing":
            for thing in updatable:
                if isinstance(thing, Enemy):
                    thing.update(player, dt, screen)
                elif isinstance(thing, Spawner):
                    thing.update(dt, screen)
                elif isinstance(thing, Player):
                    thing.update()
                elif isinstance(thing, Score):
                    thing.update(spawner.dead)
                else:
                    game_state = thing.update(timer)
            for attacker in attackable:
                for target in attackable:
                    if target is not attacker and not (isinstance(target, Enemy) and isinstance(attacker, Enemy)):
                        attacker.attacking(target, dt)
        for thing in drawable:
            if isinstance(thing, Timer):
                thing.draw(screen, dt)
            else:
                thing.draw(screen)
        #put everything on the screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
if __name__ == "__main__":
    main()
