# Uses python3
import sys
import collections




def fast_count_segments(starts, ends, points):
    start_label, point_label, end_label = 0,1,2

    labelled_points = []

    # point_to_index_map = {}
    point_to_index_map = collections.defaultdict(set)

    for p in starts:
        labelled_points.append((p, start_label))

    for i, p in enumerate(points):
        point_to_index_map[p].add(i)
        labelled_points.append((p, point_label))

    for p in ends:
        labelled_points.append((p, end_label))

    labelled_points.sort(key = lambda p: (p[0], p[1]))

    # count
    count_array = [0]*len(points)

    counter=0
    for p in labelled_points:
        if p[1] == start_label:
            counter+=1

        if p[1] == end_label:
            counter-=1

        if p[1] == point_label:
            indices = point_to_index_map[p[0]]
            for i in indices:

                count_array[i] = counter

    return count_array




def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # print(fast_count_segments([0,7], [5,10], [1,6,11])==[1,0,0])
    # print(fast_count_segments([-10], [10], [-100,100,0])==[0,0,1])
    # print(fast_count_segments([0,-3,7], [5,2,10], [1,6])==[2,0])

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
