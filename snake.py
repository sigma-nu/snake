import sys
import pygame
import random

# Snake!
#
# Recreating Snake using an object orientated approach.
#
# Future improvements:
# 1. Have a score tracker
#    - Maybe even implement something that keeps track of high-scores?

pygame.init()
pygame.display.set_caption("Snake")

# Frame rate
FPS = 5
clock = pygame.time.Clock()

# Window size
size = width, height = 600, 600
res = 50
rows = int(height/res)
cols = int(width/res)

# Initialize screen
screen = pygame.display.set_mode(size)

# Colours
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
purple = 50, 0, 100
l_grey = 220, 220, 220

# Main code -----
class Snake():
    def __init__(self):
        self.pos = [0, 0]
        self.vel = [1, 0]
        self.body = [self.pos]

    def update(self):
        self.pos = vecSum(self.pos, self.vel)
        self.cycleTail()
        return self.pos

    def cycleTail(self):
        if not grow:
            del self.body[0]
        self.body.append(self.pos)

    def draw(self):
        draw(self.body[-1], purple)
        for i in range(len(self.body)-1):
            draw(self.body[i], black)

class Food():
    def __init__(self, pos):
        self.pos = pos

    def draw(self):
        draw(self.pos, red)

def vecSum(l1, l2):
    return [a + b for a, b in zip(l1, l2)]

def draw(pos, colour):
    x = pos[0]*res
    y = pos[1]*res
    pygame.draw.rect(screen, colour, (x+2, y+2, res-2, res-2))

def spawnFood():
    pos = [random.randint(0, cols-1), random.randint(0, rows-1)]
    if pos not in snake.body:
        return Food(pos)
    return spawnFood()

def isFail():
    if snake.pos[0] >= cols or snake.pos[0] < 0:
        return True
    if snake.pos[1] >= rows or snake.pos[1] < 0:
        return True
    if snake.pos in snake.body[:-1]:
        return True
    return False

# Run -----
snake = Snake()
food = spawnFood()
while True:
    clock.tick(FPS)

    screen.fill(l_grey)
    food.draw()
    snake.draw()

    if isFail():
        snake = Snake()
        food = spawnFood()
        for i in range(2):
            clock.tick(FPS)
        continue

    
    grow = False
    if snake.pos == food.pos:
        grow = True
        food = spawnFood()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP: grow = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT : snake.vel = [-1, 0]
            if event.key == pygame.K_RIGHT: snake.vel = [1, 0]
            if event.key == pygame.K_UP   : snake.vel = [0, -1]
            if event.key == pygame.K_DOWN : snake.vel = [0, 1]
    
    snake.update()

    pygame.display.flip()