import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

rad = 300

def draw_spirograph(gap, color, circle):
    for _ in range(int(360 / gap)):
        tim.color(color)
        tim.circle(circle)
        tim.setheading(tim.heading() + gap)

while(1):
    rad -=30
    draw_spirograph(9, random_color(), rad)
    #draw_spirograph(9, "white", rad)

