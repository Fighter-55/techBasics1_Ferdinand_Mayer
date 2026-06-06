import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
image = pygame.image.load("bier.png")
IMAGE_SIZE = (200, 200)
image = pygame.transform.scale(image, IMAGE_SIZE)

class BottleOfBeer:
    def __init__(self):
        self.image = image
        size = random.randint(100, 300)
        self.size = (size, size)
        self.image = pygame.transform.scale(image, self.size)
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 200)
        self.speed_x = random.randint(2, 8)
        self.speed_y = random.randint(2, 8)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + 200 > 800:
            self.speed_x = -self.speed_x
        if self.y + 200 > 600:
            self.speed_y = -self.speed_y
        if self.x < 0:
            self.speed_x = -self.speed_x
        if self.y < 0:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

bottles = [BottleOfBeer() for _ in range(5)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for bottle in bottles:
        bottle.update()
        bottle.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# For this assignment I learned the basics of Pygame and object oriented programming.
# I had never used Pygame before, so I started with a simple window and built up from there.
# The biggest challenge was understanding how a class works in practice - especially __init__, update() and draw().
# I also learned about the game loop and why the order of operations matters (fill, update, draw, flip).
# With the help of Claude I fixed issues like nested methods, wrong indentation and the self.size problem.
# The random variables for position and speed make every run look different, which was satisfying to implement.