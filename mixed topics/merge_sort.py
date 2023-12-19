def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j=j+1
        else:
            result.append(left[i])
            i=i+1
    result.extend(right[j:])
    result.extend(left[i:])
    return result



def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2

        left=arr[:mid]
        right=arr[mid :]
        merge_sort(left)
        merge_sort(right)
        arr[:]=merge(left,right)



arr=[38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)
