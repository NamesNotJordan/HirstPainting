import turtle
import random

turtle.colormode(255)
leo =turtle.Turtle()
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204)]

leo.speed('fastest')
leo.hideturtle()
leo.up()
leo.seth(180)
leo.forward(100)
leo.setheading(255)
leo.forward(250)
leo.setheading(0)

num_dots = 100

for dot_count in range(1,num_dots):
    leo.dot(20, random.choice(color_list))
    leo.forward(50)

    if dot_count % 10 == 0:
        leo.setheading(90)
        leo.forward(50)
        leo.setheading(180)
        leo.forward(500)
        leo.setheading(0)