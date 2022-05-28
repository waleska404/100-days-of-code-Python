from turtle import Turtle, Screen
import random

colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", 
"cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

tim = Turtle()
tim.shape("turtle")
tim.color("purple")

s = Screen()
s.bgcolor("ghost white")

tim.pu()
tim.left(90)
tim.forward(300)
tim.right(90)
tim.pd()

w = 2

tim.speed(10)



while(1):
    tim.width(w)
    for i in range(3, 11):
        angle = 360/i
        tim.color(colours[i-3])
        for j in range(i):
            tim.right(angle)
            tim.forward(100)
    w += 6


s.exitonclick()