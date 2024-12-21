# Hey there! My name is Zeeshan Zahoor,
# Lets have fun by Drawing the iron man helmet using python turtle.

# Importing turtle library
import turtle

# Creating a turtle object
t = turtle.Turtle()
t.pencolor('black')  # Setting the pen color to black
t.pensize(6)  # Setting the pen size to 6
t.speed(0)  # Setting the speed of the turtle to the maximum
t.up()  # Lifting the pen so no drawing occurs


# function to draw the Outer shell of the Helmit.
def draw_outer_helmet_shell():			
    # Start drawing the outer helmet
	t.begin_fill()  # Start filling the color
	t.fillcolor('red')  # Set the fill color to red
	t.up()
	t.goto(0, 300)  # Move the turtle to the starting position
	t.down()
	t.right(90)  # Rotate 90 degrees to the right
	t.forward(0)  # Move forward by 0 units (no movement)
	t.up()
	t.goto(0, 300)  # Move back to the starting position
	t.down()
	t.setheading(0)  # Set the turtle's heading to 0 (facing right)
	t.forward(110)  # Move forward by 110 units
	t.right(8)  # Rotate 8 degrees to the right
	t.forward(80)  # Move forward by 80 units
	t.right(65)  # Rotate 65 degrees to the right

	# First curved part of the helmet
	for i in range(75):
		t.forward(6)
		t.right(1/3)  # Rotate slightly right
	for j in range(40):
		t.forward(6)
		t.right(1)  # Rotate slightly more right
		
	t.right(80)  # Rotate 80 degrees to the right
	t.forward(50)  # Move forward by 50 units
	t.setheading(180)  # Set the turtle's heading to 180 (facing left)
	t.forward(78)  # Move forward by 78 units

	# Doubling (mirror the process for the other side)
	t.up()
	t.goto(0, 300)  # Move back to the starting position
	t.down()
	t.setheading(180)  # Set heading to 180 (facing left)
	t.forward(110)  # Move forward by 110 units
	t.left(8)  # Rotate 8 degrees to the left
	t.forward(80)  # Move forward by 80 units
	t.left(65)  # Rotate 65 degrees to the left
	# Second curved part of the helmet
	for k in range(75):
		t.forward(6)
		t.left(1/3)  # Rotate slightly left
	for l in range(40):
		t.forward(6)
		t.left(1)  # Rotate slightly more left
	t.left(80)  # Rotate 80 degrees to the left
	t.forward(50)  # Move forward by 50 units
	t.setheading(0)  # Set heading back to 0 (facing right)
	t.forward(78)  # Move forward by 78 units
	t.end_fill()  # Finish filling the color for the helmet
	# #round head completed
draw_outer_helmet_shell()