import turtle as t
import random


tim = t.Turtle()

screen = t.Screen()
screen.setup(width=600, height=600)

colours = ["yellow", "gold", "orange", "red", "violet", "magenta", "purple", "blue", "skyblue", 
"cyan", "turquoise", "lightgreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def check_bounds():
    if tim.xcor() <= -300:
        tim.setheading(0)
        tim.forward(100)
    elif tim.xcor() >= 300:
        tim.setheading(180)
        tim.forward(100)
    if tim.ycor() <= -300:
        tim.setheading(90)
        tim.forward(100)
    elif tim.ycor() >= 300:
        tim.setheading(270)
        tim.forward(100)

while(1):
    tim.color(random.choice(colours))
    check_bounds()
    tim.forward(30)
    tim.setheading(random.choice(directions))


