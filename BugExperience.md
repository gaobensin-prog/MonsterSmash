v0.0.0
Bugs on (9/1/2026):

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