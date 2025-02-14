"""
This time we want to write calculations using functions and get the results. Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""
def zero(operation=None):
    return operation(0) if operation else 0

def one(operation=None):
    return operation(1) if operation else 1

def two(operation=None):
    return operation(2) if operation else 2

def three(operation=None):
    return operation(3) if operation else 3

def four(operation=None):
    return operation(4) if operation else 4

def five(operation=None):
    return operation(5) if operation else 5

def six(operation=None):
    return operation(6) if operation else 6

def seven(operation=None):
    return operation(7) if operation else 7

def eight(operation=None):
    return operation(8) if operation else 8

def nine(operation=None):
    return operation(9) if operation else 9

def plus(right_operand):
    return lambda left_operand: left_operand + right_operand

def minus(right_operand):
    return lambda left_operand: left_operand - right_operand

def times(right_operand):
    return lambda left_operand: left_operand * right_operand

def divided_by(right_operand):
    return lambda left_operand: left_operand // right_operand