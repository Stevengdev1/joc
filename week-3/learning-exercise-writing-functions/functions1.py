# Week 3 Day 1
# PDF worksheet titled: 02.LE-WritingFunctions 1
# Steven Daniel

def add(x, y):
    return x + y;

def multiply(n, m):
    return  n * m;

a = eval(input("Please enter a number: "))
b = eval(input("Please enter a number: "))
print("Sum", add(a, b), "Product:", multiply(a, b))


def f(x):
    x = x-1
    return g(x)+1

def g(x):
    return x*2

def h(x):
    if x%2 == 1:
        return f(x) + x
    else:
        return f(f(x))

print(h(3))