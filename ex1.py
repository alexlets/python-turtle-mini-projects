import random
import turtle as t

tim = t.Turtle()

t.colormode(255)

for sides in range(3,11):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.color(r,g,b)
    angle = 360 / sides
    # print(f"Sides: {sides}, Angle: {angle}")
    for i in range(sides):
        tim.forward(100)
        tim.left(angle)

t.exitonclick()
