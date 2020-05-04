# Uses python3
import sys
"""
def merge(a, left, middle, right):
    left_copy = a[left:middle+1]
    right_copy = a[middle+1:right+1]

    left_idx=0
    right_idx=0
    sorted

    while left_idx <= len(left_copy) and right_idx <= len(right_copy):
        if left_copy[left_idx] <= right_copy[right_idx]


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    merge(a,left,ave,right)
    return number_of_inversions
"""

"""
4,1
3,1
9,1
5,1
4,1
5,4
9,4
9,5
4,3

439541
439   541
43  9 54  1
4 3 9 5 4 1
34 9  45 1
349   145
134459

1*1
1*1
1*2
1*3
1*1

4,3
5,4
4,1
3,1
9,5
"""
def get_number_of_inversions(a):

    inv_c = 0

    if len(a)>1:
        mid = len(a) // 2
        left_side = a[:mid]
        right_side = a[mid:]

        inv_c += get_number_of_inversions(left_side)
        inv_c += get_number_of_inversions(right_side)

        a.clear()
        while len(left_side)>0 and len(right_side)>0:
            # print(left_side[0], right_side[0])
            if left_side[0] <= right_side[0]:
                a.append(left_side.pop(0))
            else:
                # inversions += len(left_side)
                # inv += len(left_side)
                inv_c += len(left_side)
                a.append(right_side.pop(0))


        a.extend(left_side)
        a.extend(right_side)
        return inv_c
        # return left_invs+right_invs
    else:
        return 0


if __name__ == '__main__':
    # a = [4,3,9,5,4,1]
    # inv = get_number_of_inversions(a)
    # print(inv)
    # print(inversions)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # b = n * [0]
    print(get_number_of_inversions(a))
