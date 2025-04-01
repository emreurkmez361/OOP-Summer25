# 1. Naming Conventions

# Correct
student_name = "John"  # snake_case for variables
def calculate_average():  # snake_case for functions
    pass

# Wrong
StudentName = "John"  # wrong
def CalculateAverage():  # wrong


# 2. Indentation (4 spaces per level)

# Correct
def greet(name):
    print(f"Hello, {name}")

# Wrong
def greet(name):
  print(f"Hello, {name}")  # wrong - only 2 spaces


# 3. Line Length (max 79 characters)

# Correct
message = "This is a reasonably short line of text in Python."

# Wrong
long_message = "This is a very long line that goes beyond the recommended line length of 79 characters, which is bad."


# 4. Blank Lines

# Correct
def func1():
    pass


def func2():
    pass

# Wrong
def func3():
    pass
def func4():
    pass  # no blank line between functions


# 5. Imports

# Correct
import os
import sys

# Wrong
import sys, os  # multiple imports on one line


# 6. Spacing

# Correct
x = 5
y = 10
z = x + y

# Wrong
x=5
y= 10
z =x+y  # inconsistent spacing


# 7. Comments

# Correct
# This function prints a greeting
def greet_user():
    print("Hi!")

# Wrong
def greet_user(): #prints greeting
    print("Hi!")  # bad inline comment
