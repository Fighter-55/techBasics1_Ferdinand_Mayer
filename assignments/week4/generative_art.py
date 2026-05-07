import random
import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(width=1200, height=1000)
screen.bgcolor("black")
screen.colormode(1.0)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

t.penup()
t.goto(-500, -400)
t.pendown()

def draw_flower(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(36):
        t.pencolor(color)
        t.right(10)
        for j in range(6):
            t.forward(size)
            t.right(60)
            if j % 2 == 0:
                t.pensize(2)
            else:
                t.pensize(1)
    t.penup()
    t.goto(x, y)
    t.dot(size / 5, color)
    t.pendown()

def draw_flower_circle(num, radius, min_size, amplitude, hue_offset = 0.0):
    for idx in range(num):
        angle = (2 * math.pi / num) * idx
        hue = (idx / num + hue_offset) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        flower_x = radius * math.cos(angle)
        flower_y = radius * math.sin(angle)
        flower_size = min_size + amplitude * abs(math.sin(idx))
        draw_flower(flower_x, flower_y, flower_size, (r, g, b))

hue_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for p in range(3000):
    r, g, b = colorsys.hsv_to_rgb(random.choice(hue_values), 1.0, 1.0)
    t.penup()
    t.goto(random.randint(-1000, 1000), random.randint(-500, 500))
    t.dot(random.randint(5, 20), (r, g, b))

# middle
# mid_r, mid_g, mid_b = colorsys.hsv_to_rgb(0.0, 1.0, 1.0)
# draw_flower(0, 0, 58, (mid_r, mid_g, mid_b))

t.penup()
t.goto(0, 0)
t.pendown()
for i in range(36):
    hue_offset = 0.0
    hue = (i / 36 + hue_offset) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor((r, g, b))
    t.right(10)
    for j in range(6):
        t.forward(58)
        t.right(60)
        if j % 2 == 0:
            t.pensize(2)
        else:
            t.pensize(1)

# circle 1
draw_flower_circle(20, 200, 30, 25, hue_offset=0.0)

# circle 2
draw_flower_circle(40, 380, 20, 35, hue_offset=0.0)

# circle 3
draw_flower_circle(10, 480, 100, 0, hue_offset=0.0)

# circle 4
draw_flower_circle(8, 800, 170, 0, hue_offset=0.0)


screen.update()
turtle.done()