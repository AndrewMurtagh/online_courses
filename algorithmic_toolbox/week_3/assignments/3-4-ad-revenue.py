#Uses python3
from itertools import permutations
import sys

def max_dot_product(a, b):

    a.sort()
    b.sort()
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    """
    myb = [-2,-4,7]
    my_bs = list(permutations(myb))
    for p in my_bs:
        print(list(p))
        print(max_dot_product([1,3,-5], list(p)))

    print(max_dot_product([23], [39]) == 897)
    print(max_dot_product([1,3,-5], [-2,4,1]) == 23)
    print(max_dot_product([6,5], [-1,3]) == 13)
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
