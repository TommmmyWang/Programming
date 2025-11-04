# Turtle Artist
# Author: Tommy Wang
# Oct 28th 2025

# Initializing
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
t.speed(1000)

# Go to the initial position
t.pu()
t.goto(-150, -50)
t.pd()


# Define a recursive function to draw the picture
def snow(rec: int, size: float):
    if rec == 0:
        # Base case(recursion=0): Draw a straight line
        t.forward(size)
    else:
        # Recursive cases: Draw a line, but the middle 1/3rd would be replaced by a outward pentagon
        snow(rec - 1, size / 3)
        t.left(108)
        snow(rec - 1, size / 3)
        t.right(72)
        snow(rec - 1, size / 3)
        t.right(72)
        snow(rec - 1, size / 3)
        t.right(72)
        snow(rec - 1, size / 3)
        t.left(108)
        snow(rec - 1, size / 3)


# Running the function in different colors, creating a star-ike alignment
t.color("blue")
snow(4, 300)
t.left(144)
t.color("red")
snow(4, 300)
t.left(144)
t.color("green")
snow(4, 300)
t.left(144)
t.color("yellow")
snow(4, 300)
t.left(144)
t.color("purple")
snow(4, 300)
t.left(144)


wn.exitonclick()
