# Uses python3
def naive_calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def memo_calc_fib(n):
    memo={}
    if n not in memo:
        memo[n] = naive_calc_fib(n)
    return memo[n]





def calc_fib(n):
    table=[]
    table.append(0)
    table.append(1)
    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])
    return table[n]




n = int(input())
print(calc_fib(n))
