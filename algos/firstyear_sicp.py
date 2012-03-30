#@tailcall
def fact(x, acc=1):
    if (x > 1): return (fact((x - 1), (acc * x)))
    else:       return acc
