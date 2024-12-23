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


# function to draw the face cover of the helmet.
def draw_face_cover():
	# Drawing the inner helmet cover
	t.begin_fill()  # Begin filling the shape with color
	t.fillcolor('yellow')  # Set the fill color to yellow
	t.up()  # Lift the pen to move without drawing
	t.goto(0, 150)  # Move to the starting position of the inner helmet cover
	t.down()  # Lower the pen to start drawing

	# Start drawing the shape
	t.setheading(0)  # Set the initial heading to 0 degrees (right direction)
	t.forward(35)  # Draw the first horizontal line
	t.lt(80)  # Turn left by 80 degrees
	t.forward(135)  # Draw the slanted line to form the top part of the cover

	# Draw a curved edge
	t.setheading(180 - 178)  # Slight adjustment to create the curve
	for a in range(30):  # Create a curve using small steps
		t.forward(4)  # Move forward a small distance
		t.rt(1 / 2)  # Turn slightly right at each step

	t.rt(80)  # Turn right by 80 degrees to continue the shape
	for b in range(35):  # Create another curve
		t.forward(6)  # Move forward a larger distance for a broader curve
		t.rt(1 / 3)  # Turn slightly right at each step

	# Add more detailing to the curve
	t.lt(10)  # Slight left turn for shaping
	for c in range(20):  # Create a tight curve
		t.forward(1)  # Small forward steps for precision
		t.lt(2)  # Turn left more sharply

	# Draw a straight segment
	t.forward(70)  # Straight line extending the shape
	t.rt(10)  # Slight right turn for alignment

	# Add another curve
	for d in range(23):  # Create a curved edge
		t.forward(1)  # Small forward steps
		t.rt(2)  # Turn right more sharply

	# Extend the shape with straight and curved edges
	t.forward(30)  # Straight segment
	t.rt(8)  # Slight right turn
	for e in range(33):  # Create a broader curve
		t.forward(7)  # Larger forward steps
		t.lt(3 / 2)  # Turn left at a smaller angle

	# Complete the bottom part of the inner cover
	t.rt(60)  # Turn right for the next segment
	t.forward(70)  # Draw the vertical segment
	t.rt(90)  # Turn right again
	t.forward(60)  # Horizontal segment to connect the bottom part
	t.setheading(180)  # Turn to face the left direction
	t.forward(73)  # Complete the bottom edge

	# Doubling the inner helmet cover to create symmetry (mirror the process for the other side)
	t.up()  # Lift the pen to move without drawing
	t.goto(0, 150)  # Move to the starting position for the mirrored part
	t.down()  # Lower the pen to start drawing

	# Start drawing the mirrored shape
	t.setheading(180)  # Set the heading to 180 degrees (left direction)
	t.forward(35)  # Draw the first horizontal line
	t.right(80)  # Turn right by 80 degrees
	t.forward(135)  # Draw the slanted line to form the top part of the mirrored cover

	# Draw a curved edge in the opposite direction
	t.setheading(178)  # Adjust to create the mirrored curve
	for a in range(30):  # Create a curve using small steps
		t.forward(4)  # Move forward a small distance
		t.left(1 / 2)  # Turn slightly left at each step

	t.left(80)  # Turn left by 80 degrees to continue the shape
	for b in range(35):  # Create another curve
		t.forward(6)  # Move forward a larger distance for a broader curve
		t.left(1 / 3)  # Turn slightly left at each step

	# Add more detailing to the mirrored curve
	t.right(10)  # Slight right turn for shaping
	for c in range(20):  # Create a tight curve
		t.forward(1)  # Small forward steps for precision
		t.right(2)  # Turn right more sharply

	# Draw a straight segment
	t.forward(70)  # Straight line extending the shape
	t.left(10)  # Slight left turn for alignment

	# Add another curve in the opposite direction
	for d in range(23):  # Create a curved edge
		t.forward(1)  # Small forward steps
		t.left(2)  # Turn left more sharply

	# Extend the shape with straight and curved edges
	t.forward(30)  # Straight segment
	t.left(8)  # Slight left turn
	for e in range(33):  # Create a broader curve
		t.forward(7)  # Larger forward steps
		t.right(3 / 2)  # Turn right at a smaller angle

	# Complete the bottom part of the mirrored cover
	t.left(60)  # Turn left for the next segment
	t.forward(70)  # Draw the vertical segment
	t.left(90)  # Turn left again
	t.forward(60)  # Horizontal segment to connect the bottom part
	t.setheading(0)  # Turn to face the right direction
	t.forward(73)  # Complete the bottom edge

	# End filling the shape
	t.end_fill()  # Fill the mirrored shape with the specified color

	# Inner helmet cover (mirrored side) completed