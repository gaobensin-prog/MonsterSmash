import pygame
from constants import screen_width, screen_length
from getpictures import Picture
def main():
    #just like git init we make the game file
    pygame.init()
    #make the screen
    screen = pygame.display.set_mode((screen_width, screen_length))
    #clock system to limit the frame at which the game can run
    clock = pygame.time.Clock()
    running = True
    player_img = pygame.image.load(Picture("player.png").get_picture()).convert()
    while running:
        screen.fill("white")
        screen.blit(player_img, (0,0))
        #check what the player is clicking on in the game
        for event in pygame.event.get():
            #check if the player click the X button
            if event.type == pygame.QUIT:
                #if so turn the running to False so the while loop can stop
                running = False
        #put everything on the screen
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()
