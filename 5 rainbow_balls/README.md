# Rainbow Balls

Unlike with previous projects, where you've written all of your own code, for this assignment you will be improving an existing program! 

## Task 0: What is this Thing?
To get started, we should see what our program already does. Run the program, click on window with the animation, and see if you can figure out what the arrow keys and the spacebar do (hint: you may need to hold the arrow key for a moment for it to work, but you only need to press the spacebar once).

## Task 1: A Splash of Color
This program is already mostly finished, but it's a little dreary right now. Let's add some color, using what we learned about lists!

To add color, we need to implement the function `pick_color()`. Right now, it always returns `"white"`, but that won't do! Try changing `"white"` to another color and running your program to see what happens.

## Task 2: Color by Number
Okay, getting better... But let's make our balls a variety of colors. Whenever a new ball is created, the code gives it a number. The first ball will be 0, the second 1, the third 2, and so on. This variable is passed into our function as a parameter, `ball_number`, so we can use it to decide what color the ball with that number should be.

Change the program to alternate between two colors (you can choose whichever ones you'd like!). To do that, you should have the `pick_color()` function return one color when `ball_number` is odd, and the other color when `ball_number` is even. Remember, you can use the modulo operator (`%`) to find the remainder of one number divided by another.

## Task 3: A Taste of the Rainbow
If you look at the parameters for `pick_color()`, you should notice that the function has 2 parameters: `ball_number` and `colors`. You have already used `ball_number`. Now we'll work with `colors`, which is a list of possible colors. Update your `pick_color()` function so that instead of alternating between two colors, it alternates among the first 3 colors of the list. Remember that you can access values in a list by using their index.

## Task 4: The Full Spectrum
Two colors is good, but you know what's even better? A whole rainbow! Update your `pick_color()` function so that it goes through the full range of colors. Up to this point, you may have been using a separate `if` statement for each color. Try to complete this task without using any `if` statements. Hint: the modulo function (`%`) will again be very useful here!

## Task 5: Your True Colors
As a final task, let's make our program more interactive. On day 2 of this week, you will learn about how to get text input using windows in Turtle. If you didn't do that yet, you can try to figure it out on your own here: https://docs.python.org/3/library/turtle.html#turtle.textinput

When the program starts, the `get_possible_colors` function is called to determine what colors will be passed into `pick_color`. Update this function to ask the user to enter a series of colors instead of always returning the rainbow. If the user clicks "cancel" at any point, default to using the rainbow. You can determine if the user canceled by checking if the return value of `screen.textinput` is `None`.

Note: if you are using `ball_number % 7` in `pick_color()` your program will break if there are fewer than seven colors in your list. Instead of using a static number, use `ball_number % len(colors)` to allow this to work for any number of colors. (Recall that `len()` is a pre-built python function that returns the length of a list or string.)

## Bonus Task: Pot of Gold
Nice work completing the assignment! Now that you're done, you have a few options:
* Update the program to use your own color scheme. Note that you can change the background color by modifying the line that says `window.bgcolor("black")` and change the color of the spinner by editing the line that says `spinner.color("white")`
* Instead of having the colors loop through the rainbow, have them "bounce" back and forth along the spectrum: when you reach violet, go backwards until you reach red, and then repeat.
* Start looking at the rest of the code, and seeing if there are any other parts you can modify. What happens when you change `spawn_interval`, `ball_speed`, or `increase_rotation_step`? Add whatever features you'd like!