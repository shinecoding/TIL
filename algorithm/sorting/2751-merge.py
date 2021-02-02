def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left, right = array[:mid], array[mid:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0,0,0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]  #array.append(left[i])
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        #array맨뒷부분에 남은 가장 큰 수를 넣어준다! 만약 가장 큰 수가 left에 들어있다면 부등호식(left[]<right[])에서 i+=1 이 안 되서 left의 길이랑 일치하지 않았겠지
        array[k:] = left[i:] if i != len(left) else right[j:]
        #array += left[i:]
        #array += right[j:]
    return array


mList = []
n = int(input())
for _ in range(n):
    mList.append(int(input()))

res = merge_sort(mList)
for a in res:
    print(a)

