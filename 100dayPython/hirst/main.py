import colorgram
import turtle as t 
import random

phil = t.Turtle()
t.colormode(255)
# extract color returns a color object
#colors = colorgram.extract('100dayPython/hirst/dot.jpg', 20)

#color_list = []
#for color in range(len(colors)):
#    color = colors[color]
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    color_list.append(new_color)

color_list = [(237, 37, 114), (144, 26, 67), (238, 71, 36), (221, 163, 55), (15, 140, 88), (175, 163, 48), (32, 122, 187), (50, 189, 228), (172, 44, 94), (242, 219, 56), (80, 24, 74), (127, 190, 92), (250, 224, 0), (23, 171, 123), (191, 67, 40), (206, 132, 164)]

phil.penup()
phil.setposition(-300,-300)

num_lines = 10

for n in range(num_lines) :
    phil.setposition(-300, -300 + (n*50))
    for _ in range(num_lines):
        phil.penup()
        phil.fd(50)
        phil.color(random.choice(color_list))
        phil.dot(20)

screen = t.Screen()
screen.screensize(500,500)
screen.exitonclick()
