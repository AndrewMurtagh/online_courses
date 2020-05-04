# Uses python3
import sys

"""
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
"""

"""

9 8 7 6 5 4 3 2 1

0 x x x x x x x x

0 1 2 3 4 5 6 7 8
"""


def optimal_sequence(n):

    steps = [n]*n
    # print(steps)
    steps[0]=0
    step_from = [999]*n
    steps_taken=[]

    for i in range(0,n-1):
        this_num = n-i
        if this_num%3==0:
            div_num = this_num//3
            div_idx = n-div_num

            # steps[div_idx] = min(steps[div_idx], steps[i] + 1)
            if steps[i] + 1<steps[div_idx]:
                steps[div_idx] = steps[i] + 1
                step_from[div_idx] = this_num
        if this_num%2==0:
            div_num = this_num//2
            div_idx = n-div_num
            # steps[div_idx] = min(steps[div_idx], steps[i] + 1)

            if steps[i] + 1<steps[div_idx]:
                steps[div_idx] = steps[i] + 1
                step_from[div_idx] = this_num

        # steps[i+1] = min(steps[i+1], steps[i]+1)
        if steps[i] + 1<steps[i+1]:
            steps[i+1] = steps[i] + 1
            step_from[i+1] = this_num

    curr=1
    steps_taken.append(curr)
    while curr!=n:
        curr=step_from[n-curr]
        steps_taken.append(curr)

    # return steps[n-1], steps_taken
    return steps_taken


# print(optimal_sequence(96234))
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
