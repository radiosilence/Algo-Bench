def Factorial(x):
    res = 1
    for i in xrange(2, x + 1):
        res *= i
    return res
