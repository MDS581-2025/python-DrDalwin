# Write a program to check whether a number is positive, negative, or zero.

# TODO: Write your code here
# Example input: 5
# Example output: Positive number
# main.py
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
