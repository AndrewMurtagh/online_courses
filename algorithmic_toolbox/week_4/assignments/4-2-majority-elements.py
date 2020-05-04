# Uses python3
import sys

def get_majority_element(a, left, right):

    if left==right:
        return a[left]

    mid = left + (right-left)//2


    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid+1, right)

    if left_majority==right_majority:
        return left_majority
    else:
        l_count = sum(1 for i in range(left, right+1) if a[i] == left_majority)
        r_count = sum(1 for i in range(left, right+1) if a[i] == right_majority)


        if l_count > (right - left +1 ) / 2 :
            return left_majority
        if r_count > (right - left +1 ) / 2 :
            return right_majority
        return -1




if __name__ == '__main__':
    # print(get_majority_element([2,3, 9, 2, 2], 0,4))
    # print(get_majority_element([2,3,9,2,2],0,4))
    # print(get_majority_element([1,2,3,4],0,3))
    # print(get_majority_element([1,2,3,1],0,3))
    # print(get_majority_element([1,2,3,3,3],0,4))
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
