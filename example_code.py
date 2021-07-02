# author: elia deppe
# date: 6/6/21
#
# description: example code for variable exercises

# Saving a String to a variable.
name = 'elia'

# ----- Printing the contents of the variable.
print('my name is', name)       # using regular strings
print(f'my name is {name}')     # using f-strings

# When inserting a variable into an f-string, simply surround the name of the variable with {}
# Notice that the color of the curly braces and the variable aren't the same color as the string. This helps us
# identify what is and what isn't a string. Notice also that the curly braces aren't printed either, only the contents
# of the variable.


# ----- Saving a number to a variable.
num1 = 7
num2 = 11.5
num3 = -21

print('here are a few numbers:', num1, num2, num3)          # regular string
print(f'here are a few numbers: {num1}, {num2}, {num3}')    # f-string


# ----- Overwriting Variables (Re-Use)
num1 = 121
num2 = 4.422
num3 = -31.23   # Variables can switch types at any point, so feel free to save whatever you want to any variable!

print('here are the same variables, but now with different values:', num1, num2, num3)
print(f'here are the same variables, but now with different values: {num1}, {num2}, {num3}')


# ----- Saving the Result of an Operation to a Variable
num1 = 15 - 2
num2 = 12 / 3
num3 = -2 * 4.5

print('nums:', num1, num2, num3)
print(f'nums: {num1}, {num2}, {num3}')


# ----- Using Variables in Operations
num1 = num2 + num3
num2 = num1 - 15
num3 = num3 * 2     # You can use a variable in an operation that is assigning to itself!

print(f'nums: {num1}, {num2}, {num3}')


# ----- String Duplication
# String duplication is where you duplicate strings using multiplication.
# For example, if I wanted to duplicate 'cat' 5 times then:
print('cat' * 5)

# Yes, you're allowed to do operations in functions, remember that the result is what matters!
print('dog' * 3, 'gone' * 3)

# If you want to duplicate a string inside a variable, simply multiply the variable by a number
cash = '$'
hashtag = '#'
print(cash * 5, hashtag * 3, cash * 5)