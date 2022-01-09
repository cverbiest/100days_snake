# from https://stackoverflow.com/questions/22160615/python-make-one-turtle-object-always-above-another
import turtle
from turtle import Turtle, Screen

tri = Turtle(shape="turtle")
tri.color("black")
tri.pu()
tri.speed(0)
turtle = Turtle(shape="square")
turtle.shapesize(4)
turtle.color("pink")
turtle.pu()
turtle.speed(0)

def drag_handler(x, y):
    turtle.ondrag(None)
    turtle.goto(x, y)
    turtle.ondrag(drag_handler)

turtle.ondrag(drag_handler)

tri.bk(400)
while tri.distance(turtle) > 10:
    tri.setheading(tri.towards(turtle))
    tri.fd(5)
turtle.color('green')
screen = Screen()
screen.mainloop()