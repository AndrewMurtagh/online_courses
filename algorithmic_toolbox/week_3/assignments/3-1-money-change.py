# Uses python3
import sys

def get_change(m):
    """
    converts m euro into change with denomination 1,5, and 10.
    outputs the minimum number of coins given
    """

    if m<=0:
        return 0

    coins = [10,5,1]
    num_coins = []


    for i, c in enumerate(coins):
        if c>m:
            num_coins.append(0)
        else:
            num_of_this_coin = m // c

            m = m % c
            num_coins.append(num_of_this_coin)

    return sum(num_coins)

if __name__ == '__main__':
    """
    print(get_change(1) == 1)
    print(get_change(0) == 0)
    print(get_change(-1) == 0)
    print(get_change(2) == 2)
    print(get_change(15) == 2)
    print(get_change(17) == 4)
    print(get_change(28) == 6)
    """
    m = int(sys.stdin.read())
    print(get_change(m))
