# Uses python3
import time
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    res = 0
    previous = 0
    current  = 1

    for _ in range(2, n+1):
        res = (previous + current ) % 10
        previous = current
        current = res


    return res



if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)

    d = get_fibonacci_last_digit(n)
    print(d)
