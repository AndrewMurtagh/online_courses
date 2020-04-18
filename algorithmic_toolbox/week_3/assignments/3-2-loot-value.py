# Uses python3
from __future__ import division

import sys

def get_optimal_value(capacity, weights, values):
    if capacity==0:
        return 0.0

    if len(weights) != len(values):
        return 0.0


    index = list(range(len(weights))) # 0,1,2,3,4,...,n-1

    val_per_weight = [ v/w for v, w in zip(values, weights) ]

    index.sort(key = lambda i: val_per_weight[i], reverse=True)

    max_value = 0

    for i in index:
        if capacity==0:
            return max_value

        amount = min(capacity, weights[i]) # the amount of weight to take from the item.
        max_value += amount*(val_per_weight[i])
        capacity -= amount
    return max_value



if __name__ == "__main__":
    # print(get_optimal_value(50, [20,50,30], [60,100,120]) == 180.0000)
    # print(get_optimal_value(10, [30], [500]) ) #== 166.6667
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
