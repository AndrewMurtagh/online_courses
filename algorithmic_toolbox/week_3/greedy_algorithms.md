# Greedy algorithms

## General strategy

1. Make some greedy choice

2. Prove it is a safe move.

2. Reduce to a smaller problem

3. Iterate


Greedy first moves are usually of the form, take the minimum or the maximum, or the leftmost or rightmost, or first or the last.

Sorting is usually a good first move for greedy algorithms, which can reduce from O(n^2) to O(nlogn).


## Example

A car has a limited gas tank capacity and needs to travel from A to B. There are several stops along the way.

A greedy choice might be to: 1) refill at the closest gas station, 2) refill at the farthest reachable gas station, 3) keep going until there is no fuel.

Algorithm:

1. Go from A to G (the furthest reachable gas station).

2. Make G the new A.

3. Repeat until at B, or can't make it to new G.


## Greedy criteria

For a problem to be solved with a greedy approach, there needs to be two elements:

### Reduction to subproblem

A similar problem of a smaller size, recursive in natural.

min_refuels(A, B) = first_refill(G) + min_refuels(G, B)


### Safe move

A greedy choice is called a safe move if there is an optimal solution consistent with this first move.

If there is an optimal solution with this as the first move, then it is a safe move.



## Example

Find minimum number of groups of an integer array such that the maximum difference in the values of each group is x. Naive algorithm is to consider all partitions of the points into groups. At least, there are two groups and since each point (n points) can be in one group, or not be in one group, the runtime time is at least 2^n. The greedy algorithm has runtime O(n) (excluding sorting which can be nlog(n))

Sort first.

The approach we consider is to start each group from the first point that is not in a group, i.e. we add each point (starting from left) into the first group until the difference is exceeded. Then move onto the next point and start a new group.

We need to prove it is a safe move by showing there a solution using that as a first move is optimal.

![Grouping](https://miro.medium.com/max/2008/1*2uM913nkCCMaKuAcOyuGWw.png)

Let's assume the first solution below is an optimal solution.

If we shift the first group to the right so that it covers as many other points as possible (greedy approach), then: 1) we haven't missed any points to the left, so it is still a valid soution because all of the points are still grouped; and 2) the number of groups is the same so it is still an optimal solution.

So we have proven there is an optimal solution that is consistent with this as a safe move.

<br />

We then need to prove it can be reduced to a subproblem but that is clear to see.
