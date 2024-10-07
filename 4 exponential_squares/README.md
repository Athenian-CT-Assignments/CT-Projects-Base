# Exponential Squares

For this assignment, you're going to be writing your own version of an animation that got over a million likes on TikTok in just a few days: https://www.tiktok.com/@bouncing_ba11s/video/7298905329813687594

Watch that video (you shouldn't have to sign in - just close the sign-in window if it pops up), so that you know what you're trying to build. With just a few weeks of Python practice, you already know almost all of the code needed to recreate this video!

## Task 0: Coming out of your Shell
Just like in the Rainbow Balls assignment, you've been given a partially finished program and will need to complete it. This time, though, you're going to be changing more than just a couple functions.

Take a moment to look through the code, and make a mental note of what parts you understand and what you don't. Notice the different places where comments say `TODO`—that's where you'll be writing your code.

Then, run the code and see what it does. We're a long way from the TikTok video, but by working one step at a time we should be able to get there. As a first step, let's update the background color. Find the code that sets it to white right now (there will be a `TODO` next to it), and change it to black.

## Task 1: Square One
Run your program again. Uh oh, now we can't see anything. We'll need to update our turtle so that it's not the same color as the background. While we're at it, let's also change our turtle to be a big square. Go into the `create_new_square` function. Every time we want to add a new square to the screen, we're going to use this function get a turtle to represent that square.

Instead of just `return turtle.Turtle()`, update this function to do the following. It's recommended to complete one at a time, and check that it works:
- Create a new turtle, and store it in a variable. Set its color to white, so that you can see it against the screen while you work through these steps. Return this turtle at the end of the function.
- Lift the turtle's pen—we don't want our squares leaving trails behind! Use the `penup()` function to do this.
- Make the turtle appear as a square, instead of a turtle. You can use the `shape()` function to choose what shape your turtle appears as.
- Set the turtle's size, using the `turtlesize()` function, to be the number passed into this function.
- Make your turtle a random color. There's a `get_random_color()` function that's already been written for you to help with this. Every time it's called, it will return a new trio of random red, green, and blue values that can be used . Set your turtle's color to the result of a call to this function.

## Task 2: Getting Tilted
At this point, your program should make a big randomly-colored square that moves to the right and doesn't leave a trail. Just like the color is randomized, though, we also want the direction of each square to be picked at random. At the top of your `create_new_square` function, you should see a variable called `rotate_amount`. Each time the function is called, this will get set to a new random amount from 0 to 360, just what we need! Update your code to rotate your turtle to the left by this amount.

Hmm, our square is moving in a random direction now, but unfortunately it's also getting rotated—if we're trying to match the video, that won't do. We're going to use a little trick to fix this. The turtle `tilt()` function lets you rotate a turtle's shape by some number of degrees. If we tilt the shape by the opposite of the amount that we rotated the turtle, our squares will be squared up once again.

## Task 3: Turtles All the Way Down
Your program should now show a single randomly-colored square moving in a random direction. It's time to add more squares! To do this, we're going to need to modify our animation loop. Scroll to the bottom of the file, and read through the comments in the `while` loop.

As you can see, our animation consists of a series of frames, each 1/20 of a second. Every frame, we need to move all of our squares, and replace any that hit the edge of the screen with two new ones. That might seem like a lot to do in such a short time span, but computers are fast! Until we get up to thousands of squares, it should be able to keep up.

Currently, all of the squares are moved forward by 3 pixels each frame. What happens when you change that number to be lower or higher? Play around with it, then return it to 3.

There's also some code here to remove any squares that leave the screen, but they're not being replaced. Below the `TODO`, add code that does the following:
- Call the `get_size_of_square()` function, which has been provided for you, to figure out the size of the square that just hit the edge.
- Multiply that value by 0.6—we want the new squares to be smaller than the ones that hit the edge.
- Create two new squares, using the `create_new_square` function that you wrote and passing in the new size. Add each one to the `list_of_squares`, so that it will be animated on the next frame.

Congratulations! Your program should now match the TikTok pretty closely. You may be able to modify some of the values a little bit and get it even closer.

## Bonus Tasks

### Add your own twist
There are many directions that you can take this program. Choose one from the list below, or come up with your own!
- Make the squares change to a new random color every frame, instead of being given a color at the start. If that's too hard on the eyes, see if you can make them change every 20 frames (1 second) instead.
- If you watch the TikTok closely, you'll see that it has a border that changes its color to a darker version of whatever square last hit it. Try to add this to your program. Once you've drawn the border with turtles, you'll need to update the condition in the `for` loop to account for the extra space. Darkening the color is tricky—you may want to look up a technique online or ask your teacher.

### Re-using turtles
If you want an extra challenge, try optimizing your program so that it can display even more squares without lagging. Currently, to remove squares from the screen, we're just using `square.hideturtle()` to stop the square from rendering, and removing the square from our list so that we don't waste computing power continuing to move it. The turtle still exists, though, which means that as our program runs we'll end up with more and more "invisible" turtles hanging around. To fix this, change the game loop so that instead of creating two new turtles, you reuse one existing turtle and create one new one.

You probably still won't be able to support much more than 1024 squares, but this optimization may be very useful in other projects—for example, if the rainbow balls project didn't do this, it would start to slow down more and more the longer it ran.