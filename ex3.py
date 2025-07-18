import random
import turtle as t

tim = t.Turtle()

tim.speed(0)

t.colormode(255)

def draw_spirograph(step_angle, radius):
    num_iteration = int(360 / step_angle)
    for i in range(num_iteration + 1):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        tim.color(r, g, b)
        tim.circle(radius)
        tim.setheading(i * step_angle)

draw_spirograph(5, 100)

t.exitonclick()