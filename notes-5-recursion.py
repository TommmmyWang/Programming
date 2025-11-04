# Recursion
# Author: Tommy Wang
# Oct. 20th

# We're drawing trees (recursively)
import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
t = turtle.Turtle()

# Dictionary to hold colors
LEAF_COLORS = {
    "spring": "c28cae",
    "summer": "a8d4ad",
    "fall": "e57a44",
    "winter": "92b9bd",
}


def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color(LEAF_COLORS["spring"])
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward bramch_legth pixels
        t.forward(branch_length)
        # 2. Turn to the let and draw a -1 level tree
        t.left(45)
        draw_tree(level - 1, branch_length * 0.4)
        # 3. Turn to te right and draw a -1 level tree
        t.right(45)
        draw_tree(level - 1, branch_length * 0.6)
        t.right(45)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(45)
        t.backward(branch_length)


# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()

draw_tree(5, 100)
wn.exitonclick()
