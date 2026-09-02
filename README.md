MonsterSmash is inspired from those games where the character follows your cursor for movenment and it is a wave base system will you can upgrade your character and the levels get progressily harder as you advance.

DevLog on v0.0.0:
(9/1/2026):

5.Bug with Image not Loading on Rect() Object:

When running the game I notice that when the Spawner spawn in new Enemy classes there will be a moment where the Rect() object spawn in before the image loads so my first instinct was to move the code that load the image after the code that draw the Rect()

Code:

    pygame.draw.rect(screen, "white", self.rect)
    screen.blit(image, self.position)

However, after doing so the problem not only presist, it got worse. Now the image was not moving at all it would load in but does not follow the position of the Rect() object. But the Rect() object was still being spawned. So my next solution was to just pulg self.rect into the blit() method.

Code:

    screen.blit(screen, self.rect)

But the problem still was not solved so I asked Copliot to use the Socratic method to guide me toward the answer. It mention about I should look closely at my position that Im passing through. And then it clicked. Turn out whenever I updated the enemy to follow the player the position that is being updated was the self.position. So when the position get updated so does the position of my rect object but the picture is only being loaded in the old position therefore there was a position desycn. 

Code:

    self.position = pygame.Vector2(x, y)
    self.rect = pygame.Rect(self.position[0], self.positiom[1], 300, 200)

Wait, no the self.rect position is never being updated it only take on the value of the first instance of the self.position.

Therefore, the final solution is to take the position directly from the Rect() object and delete the self.position since it is no longer needed.

Code:

    self.rect = pygame.Rect(x, y, 300, 200)
    #player class movenment imporved example
    if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10

After, implenmenting that the problem was solved.

4.Added a Rect() to Player and Enemy Class:

This desicion was made due to the fact that I need a collision detection method
Code:

    pygame.Rect(x, y, width, height)


3.Bug with pygame.get.event() not closing when user press the close X:

Originally my plan was for the Player class update() method to check if the people is still alive if not I have it return False to the running variable named in my main.py but for some reason it breaks the pygame.get.event().

            if self.health <= 0:
                self.kill()
                running = False
        
It seem to be overwriting the if statement in the pygame.get.event().

            if event.type == pygame.QUIT:
                #if so turn the running to False so the while loop can stop
                running = False
        
So instead of doing it in the Player class I instead decide to add another if statement to see if the Player object is still in the Updatable group if not it pass False to the running variable making the game close.

            if player not in updatable:
                running = False

2.Enemy Attacking Player:

        if self.__position[0] < enemy.get_stuff("position")[0] and self.__position[1] < enemy.get_stuff("position")[1]:
            print(self.health)
            self.change_stat(self.health, enemy.attack, self.defense)
        
 Explaination:
        Logic a little flaw but the main idea of it is for the Enemy class to attack the Player class in a certain range.

    
1.Enemy Removing Themselves from the Spawner List:

        for enemy in self.list:
            if enemy.health <= 0:
                self.remove_from_list(enemy)
    
Explaination:
        The Spawner object in its draw method check if the enemy being append to the list of enemy being spawned in hp is equal to or below 0 if so delete the object from the list so that the draw method does not draw dead enemies.


(8/31/2026)
    Enemy Tracking Player:
            
            def update(self, player):
                    if self.__position[0] != player.get_stuff("position")[0]:
                        distance = player.get_stuff("position")[0] - self.__position[0]
                        if player.get_stuff("position")[0] < 0:
                            self.__position[0] -= distance
                        self.__position[0] += distance
                    if self.__position[1] != player.get_stuff("position")[1]:
                        distance = player.get_stuff("position")[1] - self.__position[1]
                        if player.get_stuff("position")[1] < 0:
                            self.__position -= distance
                        self.__position[1] += distance
My revise logic, my think behind it was that I need to first calculate the distance between the x and y for the player and enemy and then I subtract the enemy distance from the player distance. And to know to do the right -= or += i first see if the player x or y is negative if it is then the method know to subtract.

    if self.__position[0] != player.get_stuff("position")[0]:
                distance = player.get_stuff("position")[0] - self.__position[0]
                self.__position[0] += distance
            if self.__position[1] != player.get_stuff("position")[1]:
                distance = player.get_stuff("position")[1] - self.__position[1]
                self.__position[1] += distance
    Improved logic although still not there tho. I notice that the player position will never be negative otherwise the object would be outside the screen. However, the problem still reside of the enemy object sticking to the player object instead of slowly moving toward the player.

    self.__position[0] += distance * dt
    The fix was that I need to * it by dt to have it slowly move toward me instead of snapping to Player position.
    
Updating Health of Classes:
    
    if self.health <= 0:
                pygame.sprite.Sprite.kill(self)
            if self.__position[0] == player.get_stuff("position")[0] and self.__position[1] == player.get_stuff("position")[1]:
                self.change_stat(self.health, player.atk, self.defense)
Protype logic flawed because the position have to be excalt to attack.
    
    if self.health <= 0:
                self.kill()
                return
The first check in the update() method to see if the object is still alive 

    self.__list = []
            self.__dt = 0
        def update(self, dt):
            self.__dt += (dt * 100)
            if self.__dt > 1:
                enemy = Enemy(screen_width / 2, screen_length / 2)
                self.__list.append(enemy)
                self.__dt = 0
        def draw(self, screen):
            for i in range(len(self.__list)):
                if self.__list[i].health > 0:
                    self.__list[i].draw(screen)
There was a bug in the spawner class where the enemy that it spawn were killed but the image continue to stay on the screen, it was fix through the looping through the enemy in the list to make sure the dead ones dont get redraw.

    def draw(self, screen):
            alive = []
            for enemy in self.__list:
                if enemy.health > 0:
                    alive.append(enemy)
            self.__list = alive 
            for i in range(len(self.__list)):
                if self.__list[i].health > 0:
                    self.__list[i].draw(screen)
            alive = []
Addd a way to reset the the list so that it does not get too big and slow down the whole computer
