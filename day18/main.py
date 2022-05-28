import turtle as t
import random

screen = t.Screen()
screen.setup(width=600, height=600)

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

tim = t.Turtle()
tim.setheading(90)
tim.forward(100)

while(1):
    tim.forward(10)
    check_bounds()

print(round(tim.xcor(), 5))
screen.exitonclick()

