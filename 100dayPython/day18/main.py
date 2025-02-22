import turtle as t
from turtle import Screen 
import random 

phil = t.Turtle()
t.colormode(255)
phil.shape("turtle")
phil.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range(50):
    phil.color(random_color())
    phil.circle(100)
    phil.setheading(phil.heading() + 10 )

screen = Screen()
screen.exitonclick()