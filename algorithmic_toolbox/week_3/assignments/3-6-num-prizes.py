# Uses python3
import sys

def optimal_summands(n):

    """

    6
    111111
    x
     xx
       xxx

    8
    11111111111111111
    x
     xx
       xxx
          xxxx
    11111111111111111
              xxxxx--
              xxxxxx-
              xxxxxxx
    """

    if n<=2:
        return [n]

    summands = []
    curr_num = 1
    total = curr_num
    summands.append(curr_num)

    while total < n:
        next_num = curr_num + 1
        while total + next_num <= n:
            # it lands on the total or it hasn't been seen before and it won't block out next one
            if n - (total + next_num) == 0 or n - (total + next_num) > curr_num and total + next_num + (next_num+1) <= n:  # valid
                total += next_num
                curr_num = next_num
                summands.append(curr_num)
                break
            else:
                next_num += 1
    return summands

if __name__ == '__main__':
    # print(optimal_summands(6) == [1,2,3])
    # print(optimal_summands(8) == [1,2,5])
    # print(optimal_summands(1) == [1])
    # print(optimal_summands(2) == [2])
    # print(optimal_summands(3) == [1,2])
    # print(optimal_summands(4) == [1,3])
    # print(optimal_summands(5) == [1,4])
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
