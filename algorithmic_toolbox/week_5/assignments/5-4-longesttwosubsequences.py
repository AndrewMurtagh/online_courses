#Uses python3

import sys
from functools import reduce
import time
import random

def lcs2(a,b):
    if len(a)==0 or len(b)==0:
        return 0

    if a[0] == b[0]:
        return 1 + lcs2(a[1:], b[1:])
    else:
        return max(lcs2(a, b[1:]), lcs2(a[1:], b))

def lcs2_back(a,b):
    m=len(a)
    n=len(b)

    if len(a)==0 or len(b)==0:
        return 0

    if a[m-1] == b[n-1]:
        return 1 + lcs2(a[:m-1], b[:n-1])
    else:
        return max(lcs2(a, b[:n-1]), lcs2(a[:m-1], b))




def lcs2_memo(a,b):
    cache={}

    def lcs2_memo_recur(a,b):
        if len(a)==0 or len(b)==0:
            return 0

        a_key = reduce(lambda x, y: str(x)+str(y), a)
        b_key = reduce(lambda x, y: str(x)+str(y), b)
        args = (a_key, b_key)

        if args in cache:
            return cache[args]

        if a[0] == b[0]:
            cache[args] = 1 + lcs2_memo_recur(a[1:], b[1:])
        else:
            cache[args] = max(lcs2_memo_recur(a, b[1:]), lcs2_memo_recur(a[1:], b))
        return cache[args]

    return lcs2_memo_recur(a,b)



def lcs2_tablulation(a,b):
    m = len(a)
    n = len(b)

    matrix = [ [0 for _ in range(n+1)] for _i in range(m+1) ]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if i==0 or j==0:
                matrix[i][j]=0

            elif a[i-1]==b[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1

            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

    return matrix[i][j]

if __name__ == '__main__':

    """
    print(lcs2_back([2,7,5], [2,5]) == 2)
    print(lcs2_back([7], [1,2,3,4]) == 0)
    print(lcs2_back([2,7,8,3], [5,2,8,7]) == 2)
    random.seed(0)
    size = 1
    long_a = [ random.randint(0, 10) for _ in range(size)]
    long_b = [ random.randint(0, 10) for _ in range(size)]
    print(long_a)
    print(long_b)
    start_time = time.time()
    print(lcs2_memo(long_a, long_b))
    print("time: ", time.time() - start_time)
    start_time = time.time()
    print(lcs2(long_a, long_b))
    print("time: ", time.time() - start_time)
    print(lcs2_tablulation([2,7,5], [2,5]) == 2)
    print(lcs2_memo([7], [1,2,3,4]) == 0)
    print(lcs2_memo([2,7,8,3], [5,2,8,7]) == 2)
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2_tablulation(a, b))
