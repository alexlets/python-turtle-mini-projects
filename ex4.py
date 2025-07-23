import random

import colorgram
import turtle as t
#
colors = colorgram.extract("image.jpg", 10)

rgb_colors = []

for color in colors:
     r = color.rgb.r
     g = color.rgb.g
     b = color.rgb.b
     rgb_colors.append((r, g, b))

 print(rgb_colors)

# we copy those tuples here and we delete the white

t.colormode(255)
color_list = [(223, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203)]

tim = t.Turtle()

tim.speed(0)

tim.penup()
tim.hideturtle()
y = -250


for row in range(10):
    tim.goto(-250, y)
    for col in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50

screen = t.Screen()
screen.exitonclick()


