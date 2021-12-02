# FIBONACCI

# Fibonacci series of 5 is : 1 1 2 3 5

def fib(n):
    """
    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(n) = fib(n-1) + fib(n-2)
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    # fact = factorial(n-1)
    return fib(n-1) + fib(n-2)

print(fib(5))


# Fibonacci series of 5 is : 0 1 1 2 3

def fib(n):
    """
    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    fib(n) = fib(n-1) + fib(n-2)
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # fact = factorial(n-1)
    return fib(n-1) + fib(n-2)

print(fib(5))