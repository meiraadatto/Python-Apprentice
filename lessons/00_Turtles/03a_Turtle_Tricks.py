"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.begin_fill()
tina.color('blue')
for i in range(5):
    tina.left(72)
    tina.forward(120)
tina.end_fill()
tina.begin_fill()
tina.color('red')
def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(90)                              # Move tina forward by the forward distance
        tina.left(angle)                              # Turn tina left by the left turn
draw_polygon(4)                        # Draw a square

tina.end_fill()

tina.begin_fill()
tina.color('green')
tina.goto(0,100)    
tina.end_fill()                                  # Move tina to another spot on the screen
tina.begin_fill()
tina.color('yellow')
draw_polygon(5)                        # Draw a pentagon
tina.end_fill()
tina.begin_fill()
tina.color('purple')
tina.goto(-170,120)                                      # Move tina to another spot on the screen
tina.end_fill()
tina.begin_fill()
tina.color('pink')
draw_polygon(6)                        # Draw a hexagon
tina.end_fill()

turtle.exitonclick()                     # Close the window when we click on it
