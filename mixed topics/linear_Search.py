def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr = [2, 5, 7, 1, 9, 3]
target = int(input("enter the number to find : "))
result=linear_search(arr,target)
if result!=-1:
    print(f"element found at index {result}")
else:
    print("element not found")
