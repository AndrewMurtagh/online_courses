# Uses python3
import sys
import itertools

"""
for c in itertools.product(range(3), repeat=len(A)):
    sums = [None] * 3
    for i in range(3):
        sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

    if sums[0] == sums[1] and sums[1] == sums[2]:
        return 1

return 0
"""


def partition_k(arr, k):
    if k==0 or len(arr)==0 or sum(arr)%k!=0:
        return 0

    n = len(arr)


    table = [[ True for i in range(n + 1)] for j in range(sum(arr) // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        table[0][i] = True

    for i in range(1, sum(arr) // k + 1):
        table[i][0] = False

    for i in range(1, sum(arr) // k + 1):

        for j in range(1, n + 1):
            table[i][j] = table[i][j - 1]

            if i >= arr[j - 1]:
                table[i][j] = (table[i][j] or table[i - arr[j - 1]][j - 1])
    return 1 if table[sum(arr) // k][n] else 0


if __name__ == '__main__':
    # print(partition_k([3,3,3,3], 3))
    # print(partition_k([40], 3))
    # print(partition_k([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59], 3))
    # print(partition_k([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25], 3))


    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition_k(A, 3))
