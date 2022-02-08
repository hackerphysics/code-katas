'''
给定一个数组arr，输出两个下标，i、j，要求：
1. i < j
2. 在所有满足条件1的可能中 arr[j] - arr[i] 最大
3. O(n) 的时间复杂度
'''

def max_diff_index(arr):
    print(arr)
    n = len(arr)
    if n < 2 :
        print('length of arr is two small')
        return 
    min_index = 0
    max_index = 1
    left_index = 0
    right_index = 1
    for i,v in enumerate(arr):
        if v < arr[min_index]:
            min_index = i
        elif v > arr[max_index]:
            max_index = i
            right_index = i
            if min_index < right_index:
                left_index = min_index
        else:
            if v - arr[min_index] >= arr[right_index] - arr[left_index]:
                right_index = i
                left_index = min_index

    print(left_index,right_index)

## TEST

import random
a = [2]
max_diff_index(a)
a = [-1,2,3,-2,5]
max_diff_index(a)
random.seed(1)
a = [ random.randint(-10,10) for i in range(10)]
max_diff_index(a)
a = [ random.randint(-10,10) for i in range(10)]
max_diff_index(a)
a = [ random.randint(-10,10) for i in range(10)]
max_diff_index(a)
a = [ random.randint(-10,10) for i in range(20)]
max_diff_index(a)
a = [ random.randint(-10,10) for i in range(20)]
max_diff_index(a)