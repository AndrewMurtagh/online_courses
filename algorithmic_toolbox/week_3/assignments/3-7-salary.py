#Uses python3
import functools

import sys

def largest_number(a):

    def mycmp(a,b):
        return int(str(a)+str(b)) - int(str(b)+str(a))

    temp = sorted(a, key=functools.cmp_to_key(mycmp), reverse=True)
    return functools.reduce(lambda a,b: str(a)+str(b), temp)


if __name__ == '__main__':
    # print(largest_number([21,20,2]))
    # print(largest_number([1,23]))
    # print(largest_number([21,2]))
    # print(largest_number([23, 39, 92]))
    # print(largest_number([9,4,6,1,9]))

    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
