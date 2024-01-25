# Week 5 day 2
# Turtle Class Project
# Steven Daniel


 # Step 1. Draw a line
import turtle
turtle.Screen()
turtle.shape("turtle") # optional
turtle.speed(1)

    # Step 2. Draw a square (blue)
turtle.speed(2) # optional
turtle.pencolor("blue")
turtle.pensize(width=4)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)

    # Starting 2nd square procedure
turtle.penup()
turtle.forward(45)
turtle.pendown()

    # Step 3. Draw two squares
turtle.speed(2) # optional
turtle.pencolor("red")
turtle.pensize(width=4)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)

    # Step 4. Create a square function
turtle.pencolor("gray")
turtle.pensize(width=4)
def draw_square(length):
    for x in range(4):
        turtle.forward(length)
        turtle.left(90)
draw_square(length= 400)

# Step 5. Create a rectangle function
def draw_rectangle(length, width):
    for i in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

# Step 6. Draw Picture
def north_lane_mark(length, width):
    for each in range(1):
        turtle.penup()
        turtle.left(90)
        turtle.forward(140)
        turtle.pendown()
        turtle.right(90)
        draw_rectangle(length=15, width=75)
def south_lane_mark(length, width):
    for each in range(1):
        turtle.left(90)
        turtle.forward(140)
        turtle.pendown()
        turtle.right(90)
        draw_rectangle(length=15, width=75)
        turtle.penup()

# Reposition to create divider.
turtle.penup()
turtle.forward(181)
turtle.pendown()
turtle.color("orange")

# Draw road divider.
draw_rectangle(length=40, width=400)
turtle.penup()
turtle.forward(120)
turtle.left(90)
turtle.forward(25)
turtle.pendown()
turtle.right(90)

# Northbound 1st lane Split
draw_rectangle(length=15, width=75)
turtle.penup()

# Northbound 2nd lane split mark
south_lane_mark(length=15, width=75)

# Northbound 3rd lane split mark
north_lane_mark(length=15, width=75)

# turtle returns to original position.
turtle.penup()
turtle.home()

# Reposition turtle to draw lane splits
turtle.forward(90)
turtle.left(90)
turtle.forward(25)
turtle.pendown()
turtle.right(90)

# Southbound - 1st lane split mark
draw_rectangle(length=15, width=75)
turtle.penup()

# Southbound - 2nd lane split mark
south_lane_mark(length=15, width=75)

# Southbound - 3rd lane split mark
south_lane_mark(length=15, width=75)






turtle.Screen().exitonclick()