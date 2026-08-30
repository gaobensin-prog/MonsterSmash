from enemy import Enemy
from constants import screen_width,screen_length
class Spawner():
    count = 0
    while count < 50:
        for i in range(screen_length, screen_width):
            Enemy().get_stuff("position")[0] = i
            Enemy().get_stuff("position")[1] = i
            count += 1
    