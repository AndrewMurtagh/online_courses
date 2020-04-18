# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_stops = len(stops)
    stops.sort()
    stops.insert(0,0)
    stops.append(distance)

    num_refills=0
    curr_pos = 0

    while curr_pos<=num_stops:
        next_stop = curr_pos
        while next_stop<=num_stops and stops[next_stop+1]-stops[curr_pos] <= tank:
            next_stop+=1

        if next_stop==curr_pos:
            return -1
        else:
            curr_pos=next_stop
            num_refills+=1

    #ends up counting the last one as a stop
    return num_refills-1



if __name__ == '__main__':
    # print(compute_min_refills(950, 400, [200, 375, 550, 750]) == 2)
    # print(compute_min_refills(10, 3, [1, 2, 5, 9]) == -1)
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
