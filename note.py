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


# HW 3: How to understand the PingPong function implemented with high-order functions?
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(result, count, direction):
        if count >= n:
            return result
        elif num_eights(count) or count%8 == 0:
            return helper(result - direction, count+1, -direction)
        else: 
            return helper(result + direction, count+1, direction)
    return helper (1, 1, 1)

def pingpong(n):
    direction = 1
    num = 0
    while i in range(1, n+1):
        num += direction
        if num_eights(n):
            direction = 0 - direction
        elif num%8 == 0:
            direction = 0 - direction
    return num


# The count coins function (a different kind of the count_partitions problem)

Lecture 14 Tree
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return [tree1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)
    
def fib_tree(n):
    if n <= 1:
        return tree(n)