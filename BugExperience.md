v0.0.0

(9/4/2026):

1.Attritude get increase twice instead of increasing once

Solution used the pygame collidepoint()

(9/3/2026):

2. Wave class not reseting the Timer class self.time when the 10 seconds of time for upgrading is up

I was trying to set the Timer class value inside the Wave class which was not working because that means I was creating another instance of a Timer class and not the original one that exist in main.py 

Code:

    class Wave(Gameobject):
        def __init__(self,timer):
            super().__init__()
            self.timer =timer
            self.upgrade_time = 0
        def update(self, dt, time):
            if time <= 0 :
                self.upgrade_time += dt
                if self.upgrade_time >= 10:
                    self.upgrade_time = 0
                    self.timer.time = 10
                    return "playing"
                return "upgrading"
            return "playing"
Solution:

Code:

    class Wave(Gameobject):
        def __init__(self):
            super().__init__()
            self.upgrade_time = 0
        def update(self, dt, time):
            if time <= 0 :
                self.upgrade_time += dt
                if self.upgrade_time >= 10:
                    self.upgrade_time = 0
                    return "playing"
                return "upgrading"
            return "playing"

    #main.py
    if game_state == "upgrading":
            for thing in updatable:
                if isinstance(thing, Wave):
                    game_state = thing.update(dt, timer.time)
                    if game_state == "playing":
                        timer.reset_time()

After adding a extendal check the problem was resolved

1. Calling a attribute from a int object in Timer class

Code:

     self.time = time.time

Solution:

Seem like I need to switch the arguments of that method.

I was wrong I meant to pass the Timer() class into the Wave() class but end up passing Timer().time instead so it was a int.


Bugs on (9/1/2026):

6. Even When the Player Attack is set to 1000 the Enemy is somehow only taking 10 damage but when the Player is at the topleft section of the screen somehow the attack it revert by to 1000.

Explanation:

Okay so this was actually a multiple problems happening at once. Let me explain how I trace through and arrive at the solutions.

Code:

    if (
            self.rect.left * 2 <= enemy.rect.right 
            and self.rect.right * 2 >= enemy.rect.left 
            and self.rect.bottom * 2 >= enemy.rect.top 
            and self.rect.top * 2 <= enemy.rect.bottom 
        ):
            object.change_stat(object.health, self.attack, object.defs)

This was the orginal code behind the class attacking each other, not going to lie I did also asked Copilot to help me with what is going on it was suggesting that I there was so code in my codebase that revert my Player Attack to 10 and that my parent class Gameobject is actually the problem with addition to my collision logic being wrong which of the only part that it got right.

Code:

    class Gameobject(pygame.sprite.Sprite):
        def __init__(self, atk = attack, hp = health, defs = defense) -> None:
            if hasattr(self, "containers"):
                super().__init__(*self.containers)
                self.attack = atk
                self.health = hp
                self.defense = defs
            else:
                super().__init__()
                self.attack = atk
                self.health = hp
                self.defense = defs
        
        def update(self):
            raise ValueError("Each Class need its own Update() Method!")
        
        def change_stat(self, hp, atk, defs):
            new_hp = hp - (atk - defs)
            self.health = new_hp

This is the parent class of both Player and Enemy class, I knew that the child class only use the parent's attitudes when it itself did not declare one yet for example in the case of my Player class I declared its attack to be 1000 so it will never use the parent's attack stat. And against my better judgment I decide to use Copliot suggestion which is to remove the default value of the parent but I went ahead and just deleted the parameter all together.

Code:

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

And of course the problem was not fix at all because the parent class was never the problem.

Solution:

There is actually two main problems. 

First, my collision logic was dookie I figure this what when I printed the Player attack everytime it attacked and also the enemy that spawn in behind the player does not seem to be attacked by the player but they still take 10 damage per sec while the enemy that spawn in at the bottom side of the Player get attacked for the full 1000.

Second, after I realized that I figure it out the enemy was actually attacking themselves!! 

Code: 

    for attacker in attackable:
            for target in attackable:
                if target is not attacker:
                    attacker.attacking(target, dt)

This code take the first item of the attackable group as the attacker and the second item as the target the if statement only prevent them from  attacking itself but it never prevent the attacker from attacking a instance of themselves!!

The Fix:

    for attacker in attackable:
            for target in attackable:
                if target is not attacker and not (isinstance(target, Enemy) and isinstance(attacker, Enemy)):
                    attacker.attacking(target, dt)

After I added the additional check and fix up my collision logic for the player everything was fixed.


5. Collision Seem to be Off after adding a health bar to Player.

Problem my logic for the collision was not right I thought the x,y for pygame.Rect was the center turn out it was the top left so it mess my whole hitbox up. The fix was to just use the rect.right,.left.top.bottom to compare sides.

Adter some deep dive again it seem like my attempt to increase the player range by 2 times was not the right logic 

Code:

    if (
            self.rect.left * 2 <= enemy.rect.right 
            and self.rect.right * 2 >= enemy.rect.left 
            and self.rect.bottom * 2 >= enemy.rect.top 
            and self.rect.top * 2 <= enemy.rect.bottom 
        ):

To be honest, I don't fully gasp why this doesn't work it, it should just double the player reach but it doesn't
My next step is too proporty just using another Rect() object and have it be the actual reach of the Player.


Code:

    def attacking(self, player, dt):
        self.cooldown += dt
        if (
            self.rect.left <= player.rect.right
            and self.rect.right >= player.rect.left
            and self.rect.bottom >= player.rect.top
            and self.rect.top <= player.rect.bottom
            and self.cooldown >= 1
        ):
            player.change_stat(player.health, self.attack, player.defense)
            self.cooldown = 0



4. The Timer() object not being drawn.

Code:
    
    class Timer(Gameobject):
        def __init__(self):
            super().__init__()
            self.time = 100
            self.rect = pygame.Rect(10, 5, 20, 10)
        def draw(self, screen, dt):
            self.time -= dt
            time = pygame.font.Font.render(str(round(self.time)), False, "red")
            screen.blit(time, (self.rect.x, self.rect.y))

Problem:

This was my very first implenmentation the first poblem that came up was my lack of understanding of what class.containers actually accpet as a argument. So I was doing Timer.containers = (drawable) which threw me an error because it was not a tuple.

After that was resolved by doing (drawable,) to make it a tuple. Another, problem arose it was the miss use of the pygame.font.Font.render() I was rending a class object instead of a font object.

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

Solution:

It was to create a Font object then use the render() function to create a Surface object of that font which is then paste into screen.blit to displayed it on the screen.

3.Spawner class spawning enemy on a certain spot instead of spawning in a random (x,y)

When running the game the Spawner class only spawn enemy on the bottom part of the screen.

Code:

    random_x = random.randint(screen_length, screen_width)
    random_y = random.randint(screen_length, screen_width)

Problem:

Because the range for both is set to 720 to 1280 the Enemy can only spawn on the bottom of the screen.

Fix:

Therefore the solution is too just set the lower range for each to 0 and then it will spawn in random.

Code:

    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_length)



2.Bug with Image not Loading on Rect() Object:

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

1.Bug with pygame.get.event() not closing when user press the close X:

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