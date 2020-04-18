# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')



"""
-----
  -------
    -------
1-2-3-4-5-6-7-8-9
    x

##############################

      -------
-----
  -------
        ---
1-2-3-4-5-6-7-8-9
    x     x

##############################

-----
  -------
        ---
      -------
1-2-3-4-5-6-7-8-9
    x     x

"""



def optimal_points(segments):
    if segments == None:
        return []

    if len(segments)==1:
        return segments[0].end


    points = []

    segments.sort(key = lambda ele: ele[1])


    num_segs = len(segments)-1
    curr_index=0

    while curr_index<=num_segs:

        curr_seg_end = segments[curr_index][1]
        # curr_seg_end = segments[curr_index].end
        points.append(curr_seg_end)
        frontier_index = curr_index

        # while frontier_index<num_segs and segments[frontier_index+1].start <= curr_seg_end and curr_seg_end <= segments[frontier_index+1].end:
        while frontier_index<num_segs and segments[frontier_index+1][0] <= curr_seg_end and curr_seg_end <= segments[frontier_index+1][1]:
            frontier_index+=1

        curr_index=frontier_index+1


    return points



if __name__ == '__main__':
    """
    f = open('./test.txt')
    inputs =[]
    lines = f.readlines()
    for line in lines:
        asdf = line.split(' ')
        inputs.append((int(asdf[0].strip()), int(asdf[1].strip())))

    print(optimal_points(inputs) == [1, 4, 5, 8, 9, 10, 14, 15, 18, 23, 26, 28, 29, 30, 32, 34, 35, 36, 40, 41, 44, 46, 49, 52, 54, 56, 58, 61, 62, 63, 65, 67, 70, 74, 77, 78, 79, 81, 84, 87, 91, 93, 95])
    print(optimal_points([(1,3), (2,5), (3,6)]) == [3])
    print(optimal_points([(4,7), (1,3), (2,5), (5,6)]) == [3, 6])
    """
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
