# Uses python3
import sys

"""
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
 """

def optimal_weight(W, weights):
    num_items = len(weights)
    table = [ [0 for _ in range(W+1) ] for _ in range(num_items+1) ]
    # for r in table:
        # print(r)
    # print("\n")
    for i in range(num_items+1):
        for w in range(W+1):
            if i==0 or w ==0:
                table[i][w] = 0
            else:
                table[i][w] = table[i-1][w]
                if weights[i-1] <= w:
                    table[i][w] = max(table[i-1][w], table[i-1][w-weights[i-1]] + weights[i-1] )
    return table[num_items][W]
    # print(table[num_items][W])
    # for r in table:
        # print(r)

if __name__ == '__main__':
    # print(optimal_weight(10, [1,4,8]))# == 9
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
