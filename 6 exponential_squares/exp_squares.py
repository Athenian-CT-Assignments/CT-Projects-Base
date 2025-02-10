"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle
import time
from random import randint

window = turtle.Screen()

# A function written to help you, that will return a random color
# which you can pass into a turtle's color() function.
def get_random_color():
  return randint(0, 255), randint(0, 255), randint(0, 255)


# A function written to help you, that will return the size
# of the square that is passed in as a parameter.
def get_size_of_square(square):
  return square.shapesize()[0]


# A function to create a new square. Instructions for implementing
# this function are given below.
# Takes in the size that the square should be as a parameter.
def create_new_square(size):
  rotate_amount = randint(0, 360) # Ignore this until you begin Task 2.

  #############################################################
  # TODO (Task 1): Write this, following steps in the README. #
  #############################################################
  return turtle.Turtle()


# Takes in a square turtle as a parameter, and determines whether
# it's touching the edge of the screen.
def touches_edge_of_screen(square):
  return abs(square.xcor()) + square.shapesize()[0] * 10 > window.window_width() / 2 or abs(square.ycor()) + square.shapesize()[0] * 10 > window.window_height() / 2

# Set up the environment. You shouldn't need to change any of these.
turtle.tracer(0, 0) # Turns off the turtle drawing animation
turtle.colormode(255) # Makes our program use the RGB color format
window.bgcolor("white") # TODO (Task 0): Change this color
frame_rate = 20 # Determines the maximum speed that our program runs
                # With many squares on-screen, it may be slower.
time_per_frame = 1 / frame_rate

# A list containing all of the squares that are currently on the
# screen. It starts off with just a single, big square.
list_of_squares = [create_new_square(15)]

# This is what is called an "animation loop". It will run 20 times
# each second, and each time it does we will move our squares a little
# bit further, and remove or add new ones as needed.
# Our program will continue the animation loop until there are 1024
# squares on the screen. You could run it for longer, but it will
# start to get really slow!
# Each loop represents a frame (1/20 of a second).
while len(list_of_squares) <= 1024:
  frame_start_time = time.time()

  # Every frame, we need to update all of our squares.
  # Computers can (generally) only do one thing at a time,
  # so we need to loop through our list of squares and
  # handle each one individually.
  for square in list_of_squares:
    # Move the square forward in whatever direction it's facing.
    square.forward(3)

    # Check to see if the square hit the outside of the screen.
    # You can look up in this file to see how the function works!
    if touches_edge_of_screen(square):
      # Get rid of the square that just hit the outside of the screen
      square.hideturtle()
      list_of_squares.remove(square)

      #############################################################
      # TODO (Task 3): Add two new squares that are a bit smaller #
      # than the size of the square that is being removed.        #
      # Multiplying the size of the square being removed by 0.6   #
      # should be good. Hint: use the get_size_of_square() and    #
      # create_new_square() functions.                            #
      #############################################################

      # Replace this comment with your code (keep indentation!)

  window.update() # We're using a mode of turtle that only updates the
                  # screen when we call this function.
                  # Much more efficient!

  # If we updated the frame faster than a frame's length (1/20 of
  # a second), pause the program for the rest of that time.
  frame_time = time.time() - frame_start_time
  if frame_time < time_per_frame:
    time.sleep(time_per_frame - frame_time)

# After the loop is complete, the program stops drawing new frames,
# but it may appear to keep moving due to an optical illusion called
# "Motion Aftereffect".
# https://en.wikipedia.org/wiki/Motion_aftereffect

# You can use turtle to create all sorts of optical illusions!
# See more here: https://pythonturtle.academy/tag/illusion/