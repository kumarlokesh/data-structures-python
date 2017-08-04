"""
Added function to generate Fibonacci series sum using recursive approach.
Sum of all the elements till the provided position should be returned.
"""

def get_fib(position):
    if position < 0:
        return -1
    elif position in [0,1]:
        return position
    return get_fib(position-1) + get_fib(position-2)
