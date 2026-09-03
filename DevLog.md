DevLog on v0.0.0:

(9/3/2026):

1. Add Wave System

Logic:

It should inherit from the Gameobject class, and it should take in the time from the Timer class and see if it reach 0 if so pause the game, and let the Player choose a upgrade to themselves. After 30 seconds or when the Player clicked continue it should unpause the game and increase the diffcultly by increasing the spawn rate of the enemy and increasing there stats also.

Code:

    class Wave(Gameobject):
        def __init__(self):
            super().__init__()
            self.time = 0

        def update(self, timer: object):
            self.time = timer.time
            if self.time <= 0:
                pygame.time.wait(5000)
                timer.time = 15

Explanation:

Wave class is in the updatable group and when it is called the Timer class is pass into it and we extract the time from the Timer and if it is 0 we freeze everything on screen and wait for 5 sceonds then reset the timer.time back to a certain time.

Code:
    #in main.py
    game_state = "playing" # Every loop will run
    game_state = "upgrading" # only drawable group loop will run
    def update(self, timer: object):
        self.time = timer.time
        if self.time <= 0:
            return "upgrading"
        return "playing"

Explanation:

The previous illulration freeze everything in the game so that means when I need to do the upgrade system later on it would not update so with the help of Copilot a cleaner way is just to stop certin gameplay loop like the updatable and attackable when the wave ended.


(9/2/2026):

5. Add Score

Explanation:

In the Spawner class I add a new dead enemy list, I looped through the list of enemy that the spawner produce and see how much of them is dead in it and if so I append them into the new dead enemy list and return the len() them reset it.

Code: 
    #spawner class
    for enemy in self.enemy:
            if enemy.health <= 0:
                self.dead.append(enemy)
                self.enemy.remove(enemy)
    
    #score class
        def draw(self, screen):
            self.score = len(self.dead_enemy)
            self.dead_enemy = []
            font = pygame.font.Font(None, 32)
            surface = font.render("Score = " + str(self.score), False, "red")
            screen.blit(surface, (self.rect.x,self.rect.y))

The current list of dead enemy in spawner never resets, but it will when I finished my Wave class.

4. Add Healthbar to Enemy class

Same logic as the Player class Healthbar

3. Add Healthbar to Player class

Code:

    health = pygame.font.Font(None, 32)
        surface = health.render(str(round(self.health)), False, "red")
        screen.blit(surface, (self.rect_hp.x, self.rect_hp.y))

Same idea has the Timer System

2. Add Timer System

Code:

    class Timer(Gameobject):
        def __init__(self):
            super().__init__()
            self.time = 50
            self.rect = pygame.Rect(10, 5, 20, 10)
        def draw(self, screen, dt):
            self.time -= dt
            font = pygame.font.Font(None, 32)
            time = font.render(str(round(self.time)), False, "red")
            screen.blit(time, (self.rect.x, self.rect.y))

Explanation:

This Timer class will be use to determine if a wave has ended or not.

Logic:

Inherits from the Gameobject so that we can add it to a group to illerate over has a set time of 50 and a Rect() object.

In the draw method it takes two arguments a screen object and a dt float value.

Subtract dt from self.time to simulate the Timer counting down. Then use pygame.font.Font to make a font object which is then render into a surface object since the render first argument have to be a str and in order to not display a float value the value after the dt and self.time operation is rounded then change the typing to a str, which is then plug into screen.blit to display it at the Rect() object location.

1.Add Hitbox Logic

So the idea behind a hitbox is that when two object either touch the edge of each other hitbox or there Rect() object overlap with each other.

Code:
    #enemy class example
    if (
            self.rect.x - width_of_entity <= player.rect.x + width_of_entity / 2
            and self.rect.x + width_of_entity >= player.rect.x - width_of_entity / 2
            and self.rect.y - height_of_entity <= player.rect.y + height_of_entity / 2
            and self.rect.y + height_of_entity >= player.rect.y - height_of_entity / 2
        ):
            self.change_stat(self.health, player.attack, self.defense)
Explanation:

The idea is to find the point to the left most bottom and also the point to the right most top.
To do this I take the x from the class self.rect and - it by a constant variable now normally that constant variable will be / by 2 to get the actual half point width but I wanted the player class to have twice the range so I keep the width and height the orginal amount which is double the actual value for those. 

But in order to actually get the points first both width and height need to be / by 2 because the way pygame draw the Rect() is by starting at the points give and exstanding left and right by 50 if the width parameter was 100 and top and bottom by 50 if the height paremeter was 100.

Logic:

The current class least x value have to be less than or equal to target class most x value.
The current class most x value must be greater than or equal to target class mleast x value.
The current class least y value have to be less than or equal to target class most y value.
The current class most y value must be greater than or equal to target class mleast y value.

If either of these condition is false than that means the hitbox are not touching or overlapping.



(9/1/2026):

3.Added a Rect() to Player and Enemy Class:

This desicion was made due to the fact that I need a collision detection method
Code:

    pygame.Rect(x, y, width, height)

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
