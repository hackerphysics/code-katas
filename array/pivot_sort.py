'''
给定一个array/list 和一个key，只用O(N)的时间复杂度将数组变成局部有序, 从左到右分成三个区域：
[<key] [=key] [>key]
e.g.,
input: [1,3,2,5,1,2,4,-1],2
output: [1,-1,1,2,2,3,4,5]
'''

def swap(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def pivot_sort(arr,pivot):
    print('input: ',arr,pivot)
    n = len(arr)
    index_equal = -1 # 最左侧相等的数
    index_large = n
    i= 0
    while True:
        if i == index_large:
            break
        if arr[i] == pivot:
            if index_equal == -1:
                index_equal = i
            i+= 1
        elif arr[i] < pivot:
            if index_equal == -1: # 如果没有相等的
                i += 1
            else:
                swap(arr,i,index_equal)
                i += 1
                index_equal += 1
        else:
            swap(arr,i,index_large-1)
            index_large -= 1
    
    print('output:',arr)

'''
@comment
这实际上是快速排序算法中的一步
'''
### test 
import random 
random.seed(1)
arr = [random.randint(0,10) for _ in range(20)]
pivot_sort(arr,random.randint(0,10))
arr = [random.randint(0,10) for _ in range(20)]
pivot_sort(arr,random.randint(0,10))
arr = [random.randint(0,10) for _ in range(20)]
pivot_sort(arr,random.randint(0,10))
arr = [random.randint(0,10) for _ in range(20)]
pivot_sort(arr,random.randint(0,10))