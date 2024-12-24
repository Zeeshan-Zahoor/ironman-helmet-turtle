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

	
# function to draw the eyes
def draw_eyes():
	# Drawing the left eye of the Iron Man helmet
	t.color('black')  # Set the pen color to black
	t.pencolor('black')  # Set the outline color to black
	t.up()  # Lift the pen to move without drawing
	t.goto(-160, 30)  # Position the turtle to the left side of the helmet
	t.down()  # Lower the pen to start drawing

	# Start drawing the left eye
	t.setheading(0)  # Set the heading to 0 degrees (right direction)
	t.right(20)  # Slight right turn to shape the eye

	# Draw the left eye outline (a rounded rectangle)
	for i in range(4):  # Draw the four sides of the eye
		t.forward(4)  # Move forward a short distance
		t.left(1 / 2)  # Slight left turn to round the corners

	t.left(90)  # Turn left 90 degrees to form the rectangle

	# Begin filling the eye with color
	t.begin_fill()  # Start filling the shape with color
	t.fillcolor('blue')  # Set the fill color to blue
	t.forward(20)  # Draw the top side of the rectangle
	t.right(90)  # Turn right 90 degrees

	# Draw the inner part of the left eye
	for i in range(26):  # Draw the inner curve on the top
		t.forward(4)  # Move forward a short distance
		t.left(1 / 2)  # Turn left slightly for the curve

	# Draw the sides of the eye
	for i in range(26):  # Draw the vertical sides
		t.forward(4)  # Move forward a short distance
		t.left(1 / 2)  # Turn left slightly to continue the curve

	# Complete the left side by drawing the bottom of the eye
	for i in range(26):  # Complete the bottom curve
		t.backward(4)  # Move backward to close the shape
		t.rt(1 / 2)  # Turn right to continue shaping the curve

	# Add details to the left eye shape
	t.right(100)  # Turn right to shape the side
	t.forward(16)  # Move forward to extend the side of the eye
	t.right(75)  # Turn right by 75 degrees
	t.forward(75)  # Draw a long segment for the bottom
	t.right(32)  # Turn right to shape the last part of the eye
	t.forward(35)  # Draw the final segment to complete the eye

	# End the fill for the eye shape
	t.end_fill()  # Fill the inner eye with blue color

	# Drawing the right eye (mirror image of the left eye)
	t.up()  # Lift the pen to move without drawing
	t.goto(160, 30)  # Position the turtle to the right side of the helmet
	t.down()  # Lower the pen to start drawing

	# Start drawing the right eye (mirrored)
	t.setheading(180)  # Set the heading to 180 degrees (left direction)
	t.left(20)  # Slight left turn to shape the eye

	# Draw the right eye outline (a rounded rectangle)
	for g in range(4):  # Draw the four sides of the eye
		t.forward(4)  # Move forward a short distance
		t.right(1 / 2)  # Slight right turn to round the corners

	t.right(90)  # Turn right 90 degrees to form the rectangle

	# Begin filling the right eye with color
	t.begin_fill()  # Start filling the shape with color
	t.fillcolor('blue')  # Set the fill color to blue
	t.forward(20)  # Draw the top side of the rectangle
	t.left(90)  # Turn left 90 degrees

	# Draw the inner part of the right eye
	for h in range(26):  # Draw the inner curve on the top
		t.forward(4)  # Move forward a short distance
		t.right(1 / 2)  # Turn right slightly for the curve

	# Complete the right side of the eye
	t.left(100)  # Turn left to continue shaping the eye
	t.forward(16)  # Move forward to extend the side of the eye
	t.left(75)  # Turn left by 75 degrees
	t.forward(75)  # Draw a long segment for the bottom
	t.left(32)  # Turn left to shape the last part of the eye
	t.forward(35)  # Draw the final segment to complete the eye
	t.backward(35)  # Move backward to close the shape

	# End the fill for the right eye shape
	t.end_fill()  # Fill the inner eye with blue color
	t.up()  # Lift the pen to stop drawing
	# eyes completed

# function to draw the black vantilations of helmet along with mouth shape
def draw_face_vantilation_with_mouth():
	# black ventilation part 1 with left side of mouth (Iron Man helmet)
	t.pensize(5)  # Set pen size for drawing
	t.pencolor('black')  # Set pen color to black
	t.up()  # Lift pen to move without drawing
	t.goto(-183, -60)  # Move to starting point of the first ventilation part
	t.begin_fill()  # Begin filling the shape with black color
	t.fillcolor('black')  # Set fill color to black
	t.down()  # Lower the pen to start drawing
	t.setheading(0)  # Set turtle heading to 0 (right direction)
	t.rt(60)  # Turn turtle 60 degrees to the right

	# Draw first ventilation section with curved edges
	for i in range(28):  # Loop to draw curved part
		t.forward(7)  # Move forward by 7 units
		t.rt(3 / 2)  # Slightly turn right to form curve

	# Draw the next part of the ventilation shape
	t.right(90 + 67)  # Turn the turtle to the correct angle
	t.forward(205)  # Draw the long horizontal edge
	t.end_fill()  # Fill the shape with black color
	t.backward(205)  # Move backward to the starting point

	# Set the heading to 0 degrees (right direction)
	t.setheading(0)
	t.right(55)  # Turn right to form the next part of the ventilation
	t.begin_fill()  # Start filling the next part with black color
	t.fillcolor('black')  # Set fill color to black
	t.forward(60)  # Move forward to draw a line
	t.left(115)  # Turn left to shape the next part
	t.forward(75)  # Move forward to complete the next part of the ventilation
	t.setheading(0)  # Set heading to 0 degrees
	t.forward(70 + 20)  # Move forward to shape the remaining portion
	t.right(90)  # Turn right by 90 degrees
	t.fd(15)  # Move forward by 15 units

	# Going back to the original position
	t.setheading(0)
	t.bk(85)  # Move backward by 85 units
	t.setheading(175 - 115)  # Set the correct angle to continue
	t.bk(75)  # Move backward by 75 units
	t.rt(116)  # Turn the turtle right by 116 degrees
	t.bk(75)  # Move backward by 75 units to complete the shape
	t.end_fill()  # Fill the final shape with black color

	# black ventilation part 2 with right side of mouth (Iron Man helmet)
	t.pensize(5)  # Set pen size for drawing
	t.pencolor('black')  # Set pen color to black
	t.up()  # Lift pen to move without drawing
	t.goto(183, -60)  # Move to starting point for the second ventilation part
	t.begin_fill()  # Begin filling the shape with black color
	t.fillcolor('black')  # Set fill color to black
	t.down()  # Lower the pen to start drawing
	t.setheading(180)  # Set heading to 180 degrees (left direction)
	t.lt(60)  # Turn left by 60 degrees

	# Draw second ventilation section with curved edges
	for i in range(28):  # Loop to draw the curved section
		t.forward(7)  # Move forward by 7 units
		t.lt(3 / 2)  # Slightly turn left to form curve

	# Draw the next portion of the ventilation shape
	t.lt(90 + 67)  # Turn the turtle to the correct angle
	t.forward(205)  # Draw the long horizontal line
	t.end_fill()  # Fill the shape with black color
	t.backward(205)  # Move backward to starting point

	# Set heading to 180 degrees (left direction)
	t.setheading(180)
	t.lt(55)  # Turn left to continue the next section
	t.begin_fill()  # Start filling with black color
	t.fillcolor('black')  # Set fill color to black
	t.forward(60)  # Move forward to shape the next part
	t.rt(115)  # Turn right by 115 degrees to create the next segment
	t.forward(75)  # Draw the next section of the shape
	t.setheading(180)  # Set heading to 180 degrees (left direction)
	t.forward(70 + 20)  # Move forward to complete the shape
	t.lt(90)  # Turn left by 90 degrees
	t.fd(15)  # Move forward by 15 units

	# Going back to the starting position for this section
	t.setheading(180)  # Set the heading to 180 degrees (left direction)
	t.bk(65 + 20)  # Move backward by 65 + 20 units
	t.setheading(180 - (175 - 115))  # Set heading to the correct angle
	t.bk(75)  # Move backward by 75 units
	t.lt(116)  # Turn left by 116 degrees
	t.bk(75)  # Move backward by 75 units to complete the section
	t.end_fill()  # Fill the final part with black color

# defined a separate funtion to run the whole code
def run_ironman_helmet():
	draw_outer_helmet_shell()	# to draw outer helmet shell
	draw_face_cover()	# to draw inner face cover
	draw_eyes()	# to draw the eyes
	draw_face_vantilation_with_mouth() # to draw face vantilation with mouth shape

run_ironman_helmet()	# call the function to run the whole code.

t.hideturtle() # Hide the turtle to prevent any interuption in looks
turtle.done()   # Add this at the end of your code to keep the turtle window open

# Here our iron_man_helmet project is completed..
# i hope it would be appretiated..
# i would be really happy for any further suggestions
# thank you so much.