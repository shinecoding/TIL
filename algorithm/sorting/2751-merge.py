import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    array = []
    left_index, right_index = 0, 0

    while len(left) > left_index and len(right) > right_index:
        if left[left_index] < right[right_index]:
            array.append(left[left_index])  #array.append(left[i])
            left_index += 1
        else:
            array.append(right[right_index])
            right_index += 1

    while len(left) > left_index:
        array.append(left[left_index])
        left_index += 1

    while len(right) > right_index:
        array.append(right[right_index])
        right_index += 1

    return array


mList = []

n = int(sys.stdin.readline())
for _ in range(n):
    mList.append(int(sys.stdin.readline()))

res = merge_sort(mList)
for a in res:
    print(a)

