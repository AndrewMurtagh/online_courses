# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    while left<right:
        mid = left + (right-left)//2
        if a[mid] == x:
            return mid

        elif x <a[mid]:
            right = mid

        else:
            left = mid+1

    return -1

    """
    if left>=right:
        return -1

    if a[mid] == x:
        return mid
    elif x <a[mid]:
        return binary_search(a[:mid], x)
    else:
        return binary_search(a[mid+1:right], x)
    """


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    # print(linear_search([1, 5, 8, 12, 13], 8) == binary_search([1, 5, 8, 12, 13], 8))
    # print(linear_search([1, 5, 8, 12, 13], 1) == binary_search([1, 5, 8, 12, 13], 1))
    # print(linear_search([1, 5, 8, 12, 13], 23) == binary_search([1, 5, 8, 12, 13], 23))
    # print(linear_search([1, 5, 8, 12, 13], 1) == binary_search([1, 5, 8, 12, 13], 1))
    # print(linear_search([1, 5, 8, 12, 13], 11) == binary_search([1, 5, 8, 12, 13], 11))

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
