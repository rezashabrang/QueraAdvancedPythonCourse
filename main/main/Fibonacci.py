import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x

def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
n = input()
n = int(n)
for i in range (1,n+1):
    if isFibonacci(i):
        print("+", end='')
    else:
        print("-",end='')