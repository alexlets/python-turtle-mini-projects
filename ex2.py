import random
import turtle as t

tim = t.Turtle()

random_l = [0, 90, 180, 270]

t.colormode(255)
tim.speed(10)

for i in range(200):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.color(r, g, b)
    tim_heading = random.choice(random_l)
    tim.setheading(tim_heading)
    tim.pensize(int(i / 5))
    tim.forward(100)

# current_heading = tim.heading()
# print(current_heading)