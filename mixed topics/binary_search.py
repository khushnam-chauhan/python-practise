def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<= right:
        mid=(left+right)//2
        if(arr[mid])==target:
            return mid
        elif(arr[mid])<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr = [1, 2, 3, 5, 7, 9, 11, 13]
target = int(input("Enter the number to find: "))
result=binary_search(arr,target)
if result!=-1:
    print(f"element {target} is found at {result}")
else:
    print(f"element {target} not found ")