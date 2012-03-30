def fact(x):
    return x > 1 and x * fact(x - 1) or 1
