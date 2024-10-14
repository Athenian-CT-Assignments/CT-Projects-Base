# Code based on a tutorial by Stephen Gruppetta,
# https://thepythoncodingstack.substack.com/p/zen-and-the-art-of-python-turtle-animations
import time
import turtle


def pick_color(ball_number, colors):
  # TODO (Tasks 1-4): Delete this comment and add your code here
  return "white"


def get_possible_colors():
  # TODO (Task 5): Update this function
  return ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def spawn_ball(reference, ball_number, colors):
  if pool_of_balls != []:
    balls.append(pool_of_balls.pop())
    balls[-1].showturtle()
  else:
    balls.append(turtle.Turtle())
  balls[-1].shape("circle")
  balls[-1].turtlesize(0.5)
  balls[-1].penup()
  balls[-1].setposition(reference.position())
  balls[-1].setheading(reference.heading())
  balls[-1].color(pick_color(ball_number, colors))


# Change speed of rotation
def increase_anticlockwise_rotation():
  spinner.rotation_speed += increase_rotation_step


def decrease_anticlockwise_rotation():
  spinner.rotation_speed -= increase_rotation_step


def toggle_bouncing():
  window.bounce_on = not window.bounce_on


spawn_interval = 0.2
ball_speed = 4
increase_rotation_step = 0.5
frame_rate = 20
time_per_frame = 1 / frame_rate

# Set up window
window = turtle.Screen()
window.bgcolor("black")
window.tracer(0)
window.bounce_on = False

spinner = turtle.Turtle()
spinner.color("white")
spinner.rotation_speed = 0

# Spawn new balls
balls = []
pool_of_balls = []

window.onkeypress(increase_anticlockwise_rotation, "Left")
window.onkeypress(decrease_anticlockwise_rotation, "Right")
window.onkeypress(toggle_bouncing, "space")
window.listen()

# Main animation loop
spawn_timer = time.time()
number_of_balls_created = 0
possible_colors = get_possible_colors()

while True:
  # in general, use condition with while loop but turtle can have exceptions
  frame_start_time = time.time()
  spinner.left(spinner.rotation_speed)

  # Spawn new ball
  if time.time() - spawn_timer > spawn_interval:
    spawn_ball(spinner, number_of_balls_created, possible_colors)
    number_of_balls_created += 1
    spawn_timer = time.time()

  # Move all balls and clear balls that leave the screen
  for ball in balls.copy():
    ball.forward(ball_speed)

    # Check if ball has hit a screen edge
    if window.bounce_on is True:
      # Check if ball has hit left or right wall
      if abs(ball.xcor()) > window.window_width() / 2:
        angle = 180 - ball.heading()
        ball.setheading(angle)

      # Check if ball has hit top or bottom wall
      elif abs(ball.ycor()) > window.window_height() / 2:
        angle = 360 - ball.heading()
        ball.setheading(angle)
    else:  # bouncing is turned off
      if (
          abs(ball.xcor()) > window.window_width() / 2
          or abs(ball.ycor()) > window.window_height() / 2
      ):
        ball.hideturtle()
        balls.remove(ball)
        pool_of_balls.append(ball)

  window.update()
  frame_time = time.time() - frame_start_time
  if frame_time < time_per_frame:
    time.sleep(time_per_frame - frame_time)
