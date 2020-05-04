# Uses python3
import sys


def get_change(m):

    denominations = [3,1,4]
    table = [ 1e12 for _ in range(m+1) ]

    table[0]=0

    for i in range(1,m+1): #1

        #go through denominations
        for d in denominations: #1
            if d <= m:
                table[i] = min(table[i], table[i-d]+1)

    return table[m]


if __name__ == '__main__':
    # print(get_change(2)==2)
    # print(get_change(34)==9)
    m = int(sys.stdin.read())
    print(get_change(m))
