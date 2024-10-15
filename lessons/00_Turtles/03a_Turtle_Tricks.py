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
def draw_polygon(sides,size):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        tina.forward(size)                              # Move tina forward by the forward distance
        tina.left(angle)                              # Turn tina left by the left turn

def draw_triangle(x,y,size):
    tina.penup()
    tina.goto(50,10)
    tina.pendown()
    draw_polygon(3,size)

draw_triangle(50,120,200)                        # Draw a square

tina.end_fill()
tina.penup()
tina.begin_fill()
tina.goto(10,150)    
tina.pendown()
tina.end_fill()                                  # Move tina to another spot on the screen
tina.begin_fill()
tina.color('yellow')
draw_polygon(4,110)                        # Draw a pentagon
tina.end_fill()
tina.begin_fill()
tina.color('purple')
tina.penup()
tina.goto(-245,125)  
tina.pendown()                                    # Move tina to another spot on the screen
tina.end_fill()
tina.begin_fill()
tina.color('pink')
draw_polygon(6,100)                        # Draw a hexagon
tina.end_fill()
tina.color('black')
tina.write("meira was here")
turtle.exitonclick()                     # Close the window when we click on it
