# Divide and Conquer

* easier to solve multiple subproblems rather than one large one.

* solve the subproblems and combine into the overall solution.

## Requirements

* non-overlapping, same type, idependent.

since each subproblem is of the same type, then can be solved using the same approach, recursively or iteratively. Recursion has overhead.


## Recurrence Relation
is an equation recursively definiing a sequence of values, e.g. Fibonacci
`F(n) = F(n-1)+F(n-2)` where `F(0)=0` and `F(1)=1`

In D&C runtime analysis, we usually define a recurrence relation in terms of T where T is the worst-case runtime.

## Strategy

1. Create a recursive solution.

2. Define a corresponding recurrence relation `T`.

3. Determine `T(n)`: the worst case runtime.

4. Create an iterative solution.


## Linear search
Bit of a degenerate example. D&C usually _divides_ a problem where as this subtracts one from the problem size.
```
def linearSearch(A, low, high, key):
  if low>high:
    return NOT_FOUND
  if A[low] == key:
    return low
  return linearSearch(A, low+1, high, key)
```


For linearSearch we have:
`T(n) = T(n-1)+c `- a problem of size `n`, a subproblem of size `n-1` and some constant amount of work `c` (checking `low>high` and `A[low] ==k` )

The base case for an empty array is `T(0)=c`

When we look at a recursion tree of linearSearch:

Problem size                        Work
n     #####################     |   c
n-1   ####################      |   c
n-2   ###################       |   c
      ...
2      ##                       |   c
1      #                        |   c
0                               |   c
                  total work:   | sum from 0 to n of c = theta(n)

Iterative version is:
```
for i from low to high:
  if A[i] == key:
    return i
return NOT_FOUND
```

## Binary Search

Only works for sorted inputs - monotonic non-decreasing input

```
def binarySearch(A, low, high, key):

  if low>high:
    return low-1

  mid = floor(low + (high-low)/2 )

  if key < A[mid]:
    return binarySearch(A, low, mid-1, key)

  elif A[mid] == key:
    return low

  else:
    return binarySearch(A, mid+1, high, key)

```


Recurrence relation is: `T(n) = T(floor(n/2)) + c` and `T(0) = c`

Recursion tree is:

Problem size                       Work
n     ####################     |   c
n/2   ##########               |   c
n/4   #####                    |   c
      ...
2      ##                      |   c
1      #                       |   c
0                              |   c
log2(n)           total work:  | sum from 0 to log2(n) of c = theta(log(n))

Iterative version is:
```
while low>high:
  mid = floor(low + (high-low)/2 )

  if key < A[mid]:
    high = mid-1

  elif A[mid] == key:
    return mid

  else:
    low = mid+1

return low-1
```

## Polynomial multiplication

...

## The master theorem

D&C problems end up as a recurence relations. For each one we need to create a recurence tree, see how much work is done at each level and sum them.

Binary search - `T(n) = T(n/2) + O(1)` -> `T(n) = O(log n)`

Polynomial multiplication - `T(n) = 4T(n/2) + O(n)` -> `T(n) = O(n^2)`

Optimised polynomial multiplication - `T(n) = 3T(n/2) + O(n)` -> `T(n) = O(n^log2(3))`

Sometimes we get - `T(n) = 2T(n/2) + O(n)` -> `T(n) = O(nlogn)`

Master theorem tells us the big-O runtime from the recurrence relation.

If we have a recurence relation of the form:` T(n) = aT(ceiling(n/b)) + O(n^d)` where `a>0, b>1, d>=0` then:

`T(n) = O(n^d)` if `d>logb(a)`

`T(n) = O(n^d*log(n))` if `d=logb(a)`

`T(n) = O(n^logb(a))` if `d<logb(a)`

Proof uses a recursion tree.

### Trick to computing the runtime quickly:

Look at the amount of work done and the first and second level.

1. if it's the same amont of work, then it will be the same amount for each level, so we're in case 2 where the total amount of work is the amount of work at the first level `n^d` times the number of levels `log(n)`.

2. If the work done on the first level is larger than the second level, then we know the first term will dominate so we only take the first term `n^d`.

3. Else, the last term will dominate, which is the number of leaves in the recusrion tree, which is `n^logb(a)`.

# Aside

Parallel arrays are ones where the indices of each correspond to one another
english = [ house, chair]
french = [maison, chaise]
