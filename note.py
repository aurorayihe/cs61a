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