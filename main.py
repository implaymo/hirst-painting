import turtle
from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

canvas_size = turtle.screensize(200,200, "white")
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.setposition(-300, -200)




def random_color():
    """Returns random color from the color_list"""
    return random.choice(color_list)


def dot_random_color():
    """Prints a DOT with a random color from the color_list"""
    color = random_color()
    turtle.dot(20, color)


number_of_dots = 0
while number_of_dots < 100:
    # sets starting position
    for i in range(10):
        dot_random_color()
        turtle.forward(50)
        number_of_dots += 1
    # Switch lanes
    turtle.setposition(-300, -200 + (number_of_dots // 10) * 50)



screen.mainloop()
