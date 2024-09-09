import turtle
from turtle import Turtle, Screen
import random


colors = ["Red", "Blue", "Green", "SlateGray", "DarkOrchid"]
johny_rango = Turtle()
johny_rango.shape("circle")
directions = [0, 90, 180, 270]
johny_rango.pensize(2)
johny_rango.speed("fastest")
movement = [5, 15, 30, 40, 60]

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        johny_rango.color(random_color())
        johny_rango.circle(200)
        corrent_heading = johny_rango.heading()
        johny_rango.setheading(johny_rango.heading() + 5)

spirograph(5)

screen = Screen()
screen.exitonclick()







