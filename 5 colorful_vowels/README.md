# Colorful Vowels

Your goal is to write a program where a user can choose a word, and your turtle will draw out the letters of the word, with consonants in red, vowels in blue, and the letter y in green

Recommended steps:
1. Use turtle textinput (not regular input!) to get the word from the user
2. Use the .write() function to write the whole word
3. To get multiple colors, we will need to write out the letters one at a time. Use a loop to go through the letters in the word and write out each one, instead of writing the whole word at once. You may need to write some code to move the turtle, to make sure they don't overlap!
4. Now it's time to handle the vowels! You can check if a string is contained in another string like this:
```
if letter in "abc":
    # this condition will only run if letter is a, b, or c
```

Extensions:
* Add different colors and fonts for different letters, beyond just vowels
* Instead of writing in a line, write the letters in a zigzag, circle, spiral, or some other formation