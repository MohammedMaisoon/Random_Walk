import random
from turtle import *
Snake=Turtle()
colours: list[str] = ["light gray", "medium blue", "cyan", "aquamarine", "medium slate blue", "hot pink","green yellow","yellow","lime"]
moves=[0,90,180,270]
Snake.speed(100)
Snake.pensize(15)
for _ in range(200):
    Snake.color(random.choice(colours))
    Snake.forward(30)
    Snake.setheading(random.choice(moves))
screen=Screen()
screen.exitonclick()