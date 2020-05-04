#Uses python3
import sys
import math
import random
import time

def bruteforce(arr):
    min_dist = 1e12 # TODO
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            this_dist = math.sqrt((arr[j][0]-arr[i][0])**2 + (arr[j][1]-arr[i][1])**2)
            # min_dist = this_dist if this_dist<min_dist
            if this_dist<min_dist:
                min_dist = this_dist
    return min_dist


def mergesort(arr, dimension):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left, dimension)
        mergesort(right, dimension)

        arr.clear()
        while len(left)>0 and len(right)>0:
            if left[0][dimension]<=right[0][dimension]:
                arr.append(left.pop(0))
            else:
                arr.append(right.pop(0))

        arr.extend(left)
        arr.extend(right)



def min_split_dist(arr):

    mergesort(arr,1)
    min_dist = 1e12
    for i in range(len(arr)):
        for j in range(i+1, min(i+7, len(arr))):
            this_dist = math.sqrt((arr[j][0]-arr[i][0])**2 + (arr[j][1]-arr[i][1])**2)
            # min_dist = this_dist if this_dist<min_dist
            if this_dist<min_dist:
                min_dist = this_dist

    return min_dist



def minimum_distance_recur(arr):

    if len(arr)<=3:
        return bruteforce(arr)

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    min_left = minimum_distance_recur(left)
    min_right = minimum_distance_recur(right)

    min_dist = min(min_left, min_right)


    mid_point_x = arr[mid][0]
    split_points = []

    # split_points=[]
    # for p in arr:
    #     if abs(p[0] - mid_point_x) <= min_dist:
    #         split_points.append(p)

    i=mid
    while i>=0 and arr[i][0]>=mid_point_x-min_dist:
        split_points.append(arr[i])
        i-=1
    split_points.reverse()
    i=mid+1
    while i<len(arr) and arr[i][0]<=mid_point_x+min_dist:
        split_points.append(arr[i])
        i+=1


    if len(split_points)==0:
        return min_dist
    else:
        min_split_distance = min_split_dist(split_points)

        return min(min_dist, min_split_distance)




def minimum_distance(x, y):
    merged_points = list(zip(x,y))

    mergesort(merged_points, 0) # 0 is to sort by x coordinate


    return minimum_distance_recur(merged_points)


if __name__ == '__main__':

    # random.seed(0)
    # xs = []
    # ys = []
    # for i in range(int(1e5)):
    #     x = random.randint(-1e9, 1e9+1)
    #     y = random.randint(-1e9, 1e9+1)
    #     xs.append(x)
    #     ys.append(y)
    #
    #
    # start = time.time()
    # minimum_distance(xs, ys)
    # end = time.time()
    # print(end-start)
    # print(minimum_distance([0,3], [0,4]))
    # print(minimum_distance([7,1,4,7], [7,100,8,7]))
    # print(minimum_distance([4,-2,-3,-1,2,-4,1,-1,3,-4,-2], [4,-2,-4,3,3,0,1,-1,-1,2,]))
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
