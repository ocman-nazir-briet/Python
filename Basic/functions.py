# Simple Function
def sum(a, b):
    return a + b

print(sum(10, 13))


# Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))