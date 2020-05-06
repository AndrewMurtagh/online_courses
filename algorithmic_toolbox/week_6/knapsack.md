# knapsack

Knapsack can be broken into fractional (can take fractions of each item) and discrete (cannot take fractions of each item).

Discrete knapsack can be with repititions or without repititions.

Greedy algorithm can be used for fractional knapsack by picking max value to weight ratio, but doesn't work for discrete knapsack. Need to use DP.

## With repititions:

Consider an optimal solution:
------ +++ wi +++ ----- W

if we take the ith element out of this solution then the total weight is W-wi. But the remaining solution is also the optimal solution for a knapsack of total capacity of W-wi.

We can prove this by contrdiction (cut and paste trick), if there is a solution for the remaining knapsack with a higher value, then by placing wi back in we would have a solution for the original knapsack that was 'more' optimal.

This optimal substructure means we can apply DP.

The recurrence for this is: `value(w) = max(value(w-wi) + vi)`

Pseudocode:
```
value[0] = 0
for w in range(1, W):
  value[w] = 0
  for i in range(1, n): # where n is number of possible weight/value pairs
    if wi<=w:
      this_value = value(w-wi)+vi
      if this_value > value[w]:
        value[w] = this_value
return value[W]
```

runtime is O(Wn)

Can be improved with memoisation
```
if w in hastable:
  return value(w)

value[0] = 0
for w in range(1, W):
  value[w] = 0
  for i in range(1, n): # where n is number of possible weight/value pairs
    if wi<=w:
      this_value = value(w-wi)+vi
      if this_value > value[w]:
        value[w] = this_value
insert value(w) into has table with key w
return value[W]
```
memoisation can introduce more overhead than tabulisation because of function stacks.
but this version only makes the minimum number of calls required. If all wi's are multiples of some number then there is no need to compute the numbers in between them.

## Without repititions

Not the same subproblem.

Consider an optimal solution:
------ +++ wi +++ ----- W

if we take the ith element out of this solution then the total weight is W-wi. But the remaining solution is also the optimal solution for a knapsack of total capacity of W-wi. If we add back in the ith element we would get the overall optimal solution, but we have no way of knowing whether the ith element has already been used in the smaller subproblem.

Every item could be used or not used, giving the recurrence as:

`value(w,i) = max(value(w-wi, i-1) + vi, value(w, i-1))`

Pseudocode:
```
knapsack(W):
  init value(0, j) = 0 # first row to zero
  init value(w, 0) = 0 # first column to zero

  for i from 1 to n: # iterate over items
    for w from 1 to W: # iterate over weights
      value(w, i) = value(w, i-1)

      #check if we can improve it by using the ith item
      if wi <= w:
        value = value(w-wi, i-1)+vi
        if value(w,i)<val:
          value(w,i) = val
  return value(W,n)
```

# runtime
it is not actually O(nW). W is the size of the input, W is represented by bits, so the runtime is proportional to the number of bits, not the value they represent. So runtime is actually O(n*2^logW).

This is actually exponential/ pseudo-polynomial instead of true polynomial, it isn't known if a true polynomial algorithm exists.
