# Uses python3
import sys
import random

def partition3(a, l, r):
    """
    l <= k <= m1-1      less than
    m1 <= k <= m2       equal
    m2+1 <= k <= r      greater than
    """
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        # print(a)
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]

    k = j
    for i in range(j + 1, r + 1):
        # print(a)
        if a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    # a[l], a[k] = a[k], a[l]
    # print(a)

    return j,k

# print(partition3())


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    # return a
    """
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);
    """


if __name__ == '__main__':
    # print(randomized_quick_sort([4,5,4,2,4,7,2], 0, 6))
    # print(randomized_quick_sort([2,3,9,2,2],0,4))
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
