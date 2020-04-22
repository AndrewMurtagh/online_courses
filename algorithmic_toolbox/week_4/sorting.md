# Sorting

Formal description is to return a permutation of an array such that it is non-decreasing.

Speeds up searching, searching on non-sorted is linear, searching on sorted set is logarithmic.


## Selection sort

General idea:

* Keep growing sorted part of array from left.

Steps:

1. Find minimum element and swap it with first element.

2. Find minimum elemnt from second element onwards and swap it with second element.

3. Iterate through array

Pseudocode:

```
for i from 1 to n:
  min_idx = i
  for j from i+1 to n:
    min_idx = j
  swap(arr[i], arry[min_idx])
```

Properties:

* runtime does not depend on order of input data (nearly sorted, random, reversed, etc.)

* runtime: `O(n^2)`. Roughly, it is `O(n^2/2)` since the number of iterations of the inner loop is `n + n-1 + n-2 + ... + 1 `

* `O(1)` space, it sorts in place


## Merge Sort

Based on divide and conquer.

General idea:

Recursively split array into two sorted subarrays and merge them back into one sorted array.

Subarray is sorted so finding the min will be O(1) since it will be at the first index.

Pseudocode:

```
def mergesort(A):
  if n==1:
    return A

  mid = floor(n/2)

  left = mergesort(A[0 : mid]))
  right = mergesort(A[mid+1 : n])

  A' = merge(left, right)

  return A'
```

```
def merge(left, right):

  merged = array of length left.length + right.lenth

  while left and right are not empty:
    min_left_idx = 0
    min_right_idx = 0

    if left[min_left_idx] <= right[min_right_idx]:
      move left[min_left_idx] to begining of merged
    else:
      move right[min_right_idx] to begining of merged

  move ret of left or right to the end of merged

  return merged

```


Properties:

* runtime is `O(nlog(n))` since recurrence relation is `T(n) <= 2T(n/2)+O(n)`. i.e. split the array into two equal parts and go through each part



## Lower bound of comparison-based sorting algorithm

Lower bound is O(nlogn), i.e. big-omega(nlogn)

Proof is to represent as a decision tree for all elements. Each leaf is a permutation of the input array. There must be n! permutations therefore n! leafs. The number of comparisons is at least the depth of the tree. Since it is a perfect tree the number of leaves is `l = 2^d`, so `d = log2(l)`. we need to proove `log2(n!) = big-omega(nlogn)`, with some rearranging it can be done.


![decision tree](https://www.researchgate.net/publication/220366954/figure/fig3/AS:667654037700608@1536192535114/Decision-trees-for-insertion-sort-on-lists-of-size-2-and-3-respectively.png)


## Non-comparison based sorting

Can be faster than `O(nlogn)`

## Counting sort

If the values are small _integers_ then we can use counting sort to get `O(n)` time.

Count occurences of each value in a bucket then reconstruct an array based on the number of each element

Pseudocode:

```
# A[i] is at most M
def countingSort(A, N):

  count[0 : M] = 0
  for i from 1 to N:
    count[A[i]] += 1

  position[0 : M] = 0
  post[0] = 1
  for j from 2 to M:
    post[j] = pos[j-1]+count[j-1]

  for i from 1 to n:
  A'[ position[ A[i] ] ] = A[i]
  position[A[i]] +=1
```

# Quick Sort

Is comparison based so running time has `nlogn` lower bound. It is O(1) in space.

Is recursive in nature.

General idea is to choose a random element and move all elments less than six to the left and all elements larger to the right, so that the chosen element is in its final position. To sort the subarrays to the left and right, recursively call quicksort.


```
def quicksort(A, l, r):
  if l>=r:
    return

  # m is the random element which is in its final position
  m = partition(A, l, r)

  quicksort(A, l, m-1)
  quicksort(A, m+1, r)


```

For partition algorithm:

Start with pivot at `l`. Move counter `i` from `l+1` to `r` and maintain the following invariant.
`A[k] <= x for all L=1 <= k <= j` and `A[k] > x for all j+1 < k < i`

Step through for pivot of 6 at `l`:

```
Starting:
l     j   i         r
6,4,2,3,9,8,9,4,7,6,1

i is moved to 9, 9 is greater than 6 to move i onwards

l     j     i       r
6,4,2,3,9,8,9,4,7,6,1


i is moved to 4, 4 is less than than 6 so it needs to be moved to j region by swapping with j+1

l     j       i     r
6,4,2,3,9,8,9,4,7,6,1

l     j       i     r
6,4,2,3,4,8,9,9,7,6,1

Rinse and repeat until i is at r:

l           j       r,i
6,4,2,3,4,6,1,9,7,8,9

Then swap l and j+1 to move pivot to final position
```

Pseudocode:
```
def parition(A, l, r):
  pivot = A[l]
  j = l
  for i from l+1 to r:
    if A[i] <= pivot
    j += 1
    swap(A[j] and A[i])
  swap A[l] and A[j]
  return j
```

Runtime analysis:

Worst case is to choose the minimum value at each iteration, we then partition the left into a subarray of 0 and the right into n-1 so the recurrence relation is `T(n) = n + T(n-1)` so `T(n) = n+(n-1)+(n-2)+...`. This form of arthimetic series always sums to big-theta(n^2)
Worst case is big-theta(n^2)

For a perfectly balanced partition everytime, we have a recurrence relation of `T(n) = 2T(n/2) + n` which becomes big-theta(nlogn) (the same running time as the merge sort algorithm).

Choosing a random pivot element guarantees an upper bound of nlogn.

Choose a random pivot element and swap it with `l` before calling parition.

### Optimisations / Implementation Issues

* Arrays that have few equal elements optimisation:

On input arrays that have a few equal elements the running time becomes O(n^2).

Can use a three-way partition to compensate where first partition is <x, second is ==x and third is >x. Middle region is already in final place.

* Tail recursion elimination optimisation:

Can remove one of the recursive calls to quicksort at the end. It is better to remove the call with the larger parititon.

* Intro sort

Choosing a random pivot element can lead to debugging issues and different call traces on the same input. We would like a deterministic method of choosing a good pivot so we get reproducibility.

Some heuristics we can choose are: the middle element, the first, the last, or the median of the first, middle and last element


* Switch to heap sort

While we are in quicksort, maintain a counter of recursion depth and if it exceeds some threshold clog(n) then we are probably going into a pathalogical case. We have used nlog(n), switch to heap sort. Heap sort has a worst case of nlog(n) so will guarantee good performance. Quicksort is usally quicker in practice than heapsort.

## Note
`nlog(n)` can be thought of as log(n) levels and spending linear time at each level.
