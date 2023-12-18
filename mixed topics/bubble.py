

def buble(arr):
    n=len(arr)
    for i in range(n): #4
        for j in range(0,n-i-1): #for (j=0;j<n-i-1:j++) j=2 0 1 2
            if( arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [64, 25, 12, 22, 11]

print("Original array:", arr)
buble(arr)

print("Sorted array:", arr)