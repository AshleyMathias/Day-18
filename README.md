# Day-18
Dot Painting Program 🎨
This Python project uses the turtle module to create a beautiful dot painting inspired by pointillism art. The program generates a grid of colored dots with colors randomly picked from a predefined palette.

Features 🌟
Random Colors: Each dot is painted with a randomly chosen color from a curated palette.
Customizable Grid: The grid size, spacing, and dot size can be easily adjusted.
Turtle Graphics: The program uses Python's turtle module for drawing.
Prerequisites 📋
Python 3.x installed on your system.
The turtle module (pre-installed with Python).
Set your Python editor or terminal to display graphical output.
How to Run the Program 🚀
Copy the code into your Python environment.
Run the program.
A window will open displaying the dot painting. Click anywhere on the screen to close it.
Program Flow 🔄
Set Up Turtle Graphics:

The turtle module is configured with color mode 255 for RGB values.
A Turtle object (tim) is created, hidden, and positioned at the starting point of the grid.
Generate Dot Grid:

The program loops through the desired number of dots (number_dots).
Dots are drawn using the dot() method with a random color from color_list.
After completing a row, the turtle moves to the start of the next row.
End Program:

The program keeps the turtle window open until the user clicks on it.
