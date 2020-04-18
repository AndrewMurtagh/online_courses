# Fractional knapsack problem

Given the weights `wi, ..., wn` and values `vi, ..., vn` of `n` items and a capacity of a knapsack of `W`. Find the maximum value of the items that can fit in the knapsack.

Greedy choice is to look at the highest value per unit weight, and start adding that.

Prove that is is a safe move, i.e. prove there always exists an optimal solution that uses as much as possible of of an item with the maximum value to weight ratio.

Take some optimal solution (the first move):

![knapsack](https://miro.medium.com/max/2934/1*wSEbAOvlevIdWaoCbmJLTw.png)

Then take one of those items and substitute it with the higher value item, the total value of the knapsack will therefore increase.

We can see that after that move we have a similar subproblem, we have some knapsack with a capacity and some items to choose from.

## Algorithm

While the knapsack is not full:

We'll make a greedy choice by choosing the item `i` that has the highest value to weight ratio.

Put as much of `i` into the knapsack as it can fit.

Return result


## Pseudocode

```python
def fractional_knapsack(W, w, v):
  A = []
  V = []
  for i in range(n+1):
    if W==0:
      return (A, V)
    select i with w>0 (is still left) and vi/wi is max
    ai = min(wi, W) # amount to take, it is either the full amount of wi or the remaining amount of W if W is less
    V = v+  a* vi/wi
    wi = wi-a
    Ai = Ai+a
    W = W-a
  return (A,V)
```

Runtime of above is O(n^2) because of the outer loop and the inner loop to get the maximum value per weight.

We can improve it by firstly sorted by greatest v/w `list.sort(key = lambda x: x[0]/x[1], reverse=True)` if `x[i][0]` is value and` x[i][1]` is weight.

Knapsack becomes O(n) plus a sort of nlog(n), so nlog(n) 
