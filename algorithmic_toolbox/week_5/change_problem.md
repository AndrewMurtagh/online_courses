# find min number of coins to provide change

## greedy algorithm

Find the largest denomination that does not exceed the money. Use that. Subtract it from money and repeat.


```
change <- empty collection of coins
while money > 0:
  coin <- largest denomination that does not exceed money
  add coin to Change
  money -= coin
return Change
```

Greedy is not optimal, choosing the largest denomination isn't always a safe bet. To change 40 cents using 50, 25, 10 and 5 it is (25,10,5), but using 50, 20, 10 and 5 it is not (20 x 2).

## recursive approach

in order to change 40 cents using 50, 25, 10 and 5 we can start from the end and assume we know the optimal way to solve 40 - 25, 40 - 10 and 40 - 5. Then we can just add one. So:
```
minNumCoins(40) = min( minNumCoins(40-25)+1, minNumCoins(40-10)+1, minNumCoins(40-5)=1s )
```

Use this recurence to get the following pseudocode:
```
def min_num_coins(money=40, coins = [25,10,5]):
  if m==0:
    return 0
  min = 1e12
  for coin in coins:
    if coin <= money:
      num_coins = min_num_coins(money - coin, coins)
      if num_coins+1 < min:
        min = num_coins+1
  return min
```

But this has a very bad run time, 3^n.
```
          40
    /     |     \    
   15     10     35
  / \   / | \   /  \
 5  10 0  5 10  25 30
```
10 has to be computed 3 times here so what if we could save the result of `min_num_coins()` for a given input instead of recomputing it. This is Dynamic Programming (DP).

## string alignment

take `atgttata` and `atcgtcc`, how can you transform the first into the second

```

mmimmdsds
at-gttata
atcgt-c-c

where:
m is match
d is deletion
i is insertion
s is substitution
```

The 2d matrix is the alignment of the strings.

We can score the alignment by giving a score to matches, substitutions, insertions and deletions.

### longest common subsequence


### edit distance

Take an alignment between two strings:
```
A[0...i-1][i]
B[0...j-1][j]
```
Take the last element in an alignment of the two strings, i and j. It is either an insertion, deletion, substitution or a match. Say this is an optimal alignment, then the substrings up to the last element will also be optimal.

The edit distance `d` of the ith and jth element will be:
```
                                        a[i] != b[j]   a[i] == b[j]
              insertion    deletion     substitution   match
d(i,j) = min( d(i, j-1)+1, d(i-1, j)+1, d(i-1, j-1)+1, d(i-1, j-1) )
```

Implementation uses tabulation: "pho" to "ramen"
```
    '' p  h  o
''  0  1  2  3
r   1  .  .  .
a   2  .  .  .
m   3  .  .  .
e   4  .  .  .
n   5  .  .  .

return table[m][n]
```

Pseudocode:
```
a = "pho"
b = "ramen"

m = len(a)
n = len(b)

for i in range(m+1):
  for j in range(n+1):
    if from_s[i-1] == to_s[j-1]:
      table[i][j] = table[i-1][j-1]
    else:
      table[i][j] = 1+min(table[i][j-1], table[i-1][j], table[i-1][j-1])
return table[m-1, n-1]
```

You can backtrack through the table to get the optimal alignment.
