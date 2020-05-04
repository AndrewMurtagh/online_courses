#Uses python3

from functools import reduce

import sys


"""
def lcs3(a, b, c):
    cache={}

    def lcs3_inner(a,b,c):


        if len(a)==0 or len(b)==0 or len(c)==0:
            return 0

        a_key = reduce(lambda x,y: str(x)+str(y), a)
        b_key = reduce(lambda x,y: str(x)+str(y), b)
        c_key = reduce(lambda x,y: str(x)+str(y), c)
        args = (a_key, b_key, c_key)

        if args in cache:
            return cache[args]


        if a[0] == b[0] == c[0]:
            cache[args] = 1 + lcs3_inner(a[1:], b[1:], c[1:])
        else:
            cache[args] = max(lcs3_inner(a[1:], b, c), lcs3_inner(a, b[1:], c), lcs3_inner(a, b, c[1:]))
        return cache[args]

    return lcs3_inner(a,b,c)

"""

def lcs3_tabluation(a,b,c):
    m = len(a)
    n = len(b)
    o = len(c)

    matrix = [[[0 for _ in range(o+1)] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, o+1):

                if i==0 or j==0 or k==0:
                    matrix[i][j][k] = 0

                elif a[i-1] == b[j-1] == c[k-1]:
                    matrix[i][j][k] = 1 + matrix[i-1][j-1][k-1]

                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])

    return matrix[i][j][k]


if __name__ == '__main__':
    # print(lcs3_tabluation([1,2,3], [2,1,3], [1,3,5]) == 2)
    # print(lcs3_tabluation([8,3,2,1,7], [8,2,1,3,8,10,7], [6,8,3,1,4,7]) == 3)

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3_tabluation(a, b, c))
