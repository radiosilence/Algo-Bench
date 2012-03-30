import sys
import math
from time import time


def start():
    return time()


def stop(start):
    return time() - start


def bench(name, num, callback, correct):
    print "========================================================"
    print "Starting algorithm %s for %s!" % (name, num)
    print "========================================================"

    def round():
        s = start()
        newbie(num)
        return stop(s)

    rounds = 20
    time = 0
    for i in range(rounds):
        time += round()

    avg = time / rounds
    print "Did it in %s ms averaged over %s rounds." % (avg * 1000, rounds)
    print "========================================================\n"
    return avg

if __name__ == '__main__':
    try:
        r = sys.argv[1]
    except IndexError:
        r = 5000

    sys.setrecursionlimit(r * 2)

    print "Recursion limit:", sys.getrecursionlimit()

    correct = math.factorial(r)

    from algos.newbie import factorial as newbie
    bench("Newbie", r, newbie, correct)

    from algos.firstyear_pascal import factorial as firstyear_pascal
    bench("First Year Pascal", r, firstyear_pascal, correct)

    from algos.firstyear_c import fact as firstyear_c
    bench("First Year C", r, firstyear_c, correct)

    from algos.firstyear_sicp import fact as firstyear_sicp
    bench("First Year SICP", r, firstyear_sicp, correct)

    from algos.firstyear_python import Factorial as firstyear_python
    bench("First Year Python", r, firstyear_python, correct)

    from algos.lazy_python import fact as lazy_python
    bench("Lazy Python", r, lazy_python, correct)

    from algos.lazier_python import f as lazier_python
    bench("Lazier Python", r, lazier_python, correct)

    from algos.python_expert import fact as python_expert
    bench("Python Expert", r, python_expert, correct)

    from algos.python_hacker import fact as python_hacker
    bench("Python Hacker", r, python_hacker, correct)

    from algos.expert_programmer import fact as expert_programmer
    bench("Expert Programmer", r, expert_programmer, correct)

    from algos.web_designer import factorial as web_designer
    bench("Web Designer", r, web_designer, correct)

    from algos.unix_programmer import fact as unix_programmer
    bench("Unix Programmer", r, unix_programmer, correct)

    from algos.windows_programmer import fact as windows_programmer
    bench("Windows Programmer", r, windows_programmer, correct)

    from algos.enterprise_programmer import f as enterprise_programmer
    bench("Enterprise Programmer", r, enterprise_programmer, correct)
