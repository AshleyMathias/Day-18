from turtle import Turtle
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [ (235, 243, 239), (185, 161, 133), (129, 91, 70), (78, 92, 118), (147, 161, 180), (211, 207, 135), (179, 152, 163), (29, 35, 48), (49, 26, 19), (120, 81, 93), (147, 169, 154), (55, 26, 35), (165, 158, 57), (86, 106, 90), (110, 35, 47), (24, 34, 30), (171, 107, 97), (50, 58, 90), (117, 37, 29), (109, 123, 156), (161, 107, 117), (214, 178, 186), (217, 177, 172), (181, 188, 209), (107, 145, 103), (178, 202, 184), (67, 75, 38)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


number_dots = 100
for dot_count in range(1, number_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)



    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
