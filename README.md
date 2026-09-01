MonsterSmash is inspired from those games where the character follows your cursor for movenment and it is a wave base system will you can upgrade your character and the levels get progressily harder as you advance.

DevLog on v0.0.0 (8/31/26):
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
