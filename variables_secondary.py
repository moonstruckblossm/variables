# author: <name here>
# date: <date here>
#
# description: <fill in>


# Variables can be used in the same expression to assign to the variable thanks to its unique properties.
#   When we write something like:
#       x = 5
#       x = x + 1
#
#   The operation happens BEFORE the assignment. Meaning the value of x is retrieved from memory and plugged into
#   the equation x + 1 becoming 5 + 1 in this case. Then these values are added together resulting in:
#       x = 10
#
#   The assignment then takes place and the value 10 overwrites the value 5 within the memory location.
#   Python has a way we can write this in shorthand:
#       x += 1
#   Is functionally the same as:
#       x = x + 1
#
#   Subtraction is done using the - symbol instead of the +
#       x -= 1
#   Is functionally the same as:
#       x = x - 1
#
#   The rest of the assignment operators follow this format where the symbol is placed directly in front of the equals
#   sign. Check the documentation below for more information.

# --------------- Section 2 --------------- #

# 2.1 | Self Operation
#
# Relevant Documentation
#   - https://www.w3schools.com/python/gloss_python_assignment_operators.asp
#
# Variables:
#   1) Create a variable named x and set it to some value that is not 0.
#   2) Modify this variable using the assignment operators to perform operations with itelf. Complete
#   the following operations:
#       - Addition with itself and a random number.
#       - Subtraction with itself and a random number.
#       - Multiplication with itself and a random number.
#       - True or Floor Division with itself and a random number.
#       - Addition with itself and an equation
#           - Example Equation: ((10 - 2) * (4 + 3) - 1) * 15
#

