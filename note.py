# Notes during class

# Reverse Cascade
# To implement the following result
# > inverse_cascade(1234)
# > 1
# > 12
# > 123
# > 1234
# > 123
# > 12
# > 1

# Solution 1
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print(n), n//10)
shrink = lambda n: f_then_g(print(n), shrink, n//10)

# Solution 2
def inverse_cascade(n):
    def grow(n):
        if n < 10:
            print(n)
        else:
            grow(n//10)
            print(n)
    def shrink(n):
        if n < 10:
            print(n)
        else:
            print(n)
            shrink(n//10)
    grow(n)
    print(n)
    shrink(n)

# Tree recursion
# Happens when one function makes more than one recursive call
# > Example: the Fibonacci numbers
# > n: 0, 1, 2, 3, 4, 5, 6, 7, ...., 35
# > fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, ..., 9227465
# It contains a tree struction, that computing a number contains computing multiple values and has many branches,
# each branch has its own sub-branch, etc

# import a decorator that can trace the function action
from ucb import trace

@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example: Counting Partitions of an Integer
# The number of partitions of a positive integer n, using parts up to size m, is the number
# of ways in which n can be expressed as the sum of positive integer parts up to m in increasing order
# > count_partitions(partitioning_integer, maximum)
# > count_partitions(6,4)
# > 2+4=6
# > 1+1+4=6
# > 3+3=6
# > 1+2+3=6
# > 1+1+1+3=6
# ......
# Strategy:
#     1. Recursive decomposition: finding simpler instances of the problem
#     2. Explore two possibilities:
#         Use at least one 4
#         Don't use any 4
#     3. Solve two Simpler problems:
#         count_partitions(2,4)
#         count_partitions(6,3)
#     4. Tree recursion often involved exploring different choices
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m