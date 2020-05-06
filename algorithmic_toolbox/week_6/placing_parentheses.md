# Placing parentheses

Given an arithmetic expression, maximise its value by placing parentheses.

e.g.
```
1 + 2 - 3 x 4 - 5
((((1 + 2) - 3) x 4) - 5) = -5

    3    4     1    2        - order of operations
((1 + 2) - ((3 x 4) - 5) = -4


((1 + 2) - (3 x (4 - 5))) = 6 - max value
```


Naive approach is to go through all orderings. There are 4 operations, you can choose to do anyone of them first. Then you can choose to do any of the next three for the seond one, etc. It is `n!`

More strictly speaking, we have input of digits `d1, d2, di, ..., dn` and a sequence of operations `op1, op2, opi, ..., opn`. element of `{x,-,/,+}` Define an order of applying these operations to maximise the value, i.e. `d1, op1, d2, op2, ..., opn, dn`

# subproblems

Intuition, assume an operation is the last one, e.g. for `5 - 8 + 7 x 4 - 8 + 9` assume `x` is the last operation.

-> `(5 - 8 + 7) x (4 - 8 + 9)`, then we would like to know what the optimal values for both subexpressions are. But we need to know what the min and max is since -neg x -neg is +pos.

Let `Ei,j` is a subexpression between digits `i` and `j`: `di opi ... opj-1 dj`. Compute the max `M(i,j)` and min `m(i,j)`.

### recurrence relation
Four possibilities for each, split subproblems into subsubproblems at the kth operation.
```
M(i,j) = max for i<=k<j-1(
  M(i,k) opk M(k+1,j)
  M(i,k) opk m(k+1,j)
  m(i,k) opk M(k+1,j)
  m(i,k) opk m(k+1,j)
  )
```

```
m(i,j) = min for i<=k<j-1(
  M(i,k) opk M(k+1,j)
  M(i,k) opk m(k+1,j)
  m(i,k) opk M(k+1,j)
  m(i,k) opk m(k+1,j)
  )
```

### Pseudocode
Start with this function for subproblems.

```
minandmax(i,j):
  curr_min = INF
  curr_max = -INF
  for k from i to j-1:
    a = M(i, k) opk M(k+1, j)
    b = M(i, k) opk m(k+1, j)
    c = m(i, k) opk M(k+1, j)
    d = m(i, k) opk m(k+1, j)

    curr_min = min(curr_min, a, b, c, d)
    curr_max = min(curr_max, a, b, c, d)
  return curr_min, curr_max
```

When we compute subproblems we want them to already be computed so we should work through them in order of increasing j-i.
```
  j . . . n
i 1 6 x x N this is our answer since we have gone through i=1 to j=n
. x 2 7 x x
. x x 3 8 x this ....
. x x x 4 9 this diagonal has j-i = 1
n x x x x 5 this diagonal has j-i = 0
```

Algorithm maintains two tables for min and max.

```
placeParanetheses(d1, op1, d2, op2, ... dn, opn)
  for i from 1 to n:
    m(i,i) = di
    M(i,i) = di

  for s from 1 to n-1:
    for i from 1 to n-s:
      j = i+s
      m(i,j), M(i,j) = minandmax(i,j)

  return M(1,n)
```

The diagonals get filled in with their respective digit, e.g `5 - 8 + 7 x 4 - 8 + 9` becomes:
```
5   -13 .   .   .   .
.   8   15  .   .   .
.   .   7   28  .   .
.   .   .   4   -4  .
.   .   .   .   8   17
.   .   .   .   .   9
```
The second diagonal corresponds to the operation between the two digits since nothing else can be done but apply it to them.

Runtime is `O(n^3)`

The solution for what parantheses can be unrolled.
