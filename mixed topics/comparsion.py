import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time_complexity(sort_function, input_array):
    return timeit.timeit(lambda: sort_function(input_array.copy()), number=10)

# Number of elements in the array
array_size = 1000

# Generate a random array
random_array = generate_random_array(array_size)

# Measure time complexity for each sorting algorithm
bubble_sort_time = measure_time_complexity(bubble_sort, random_array)
insertion_sort_time = measure_time_complexity(insertion_sort, random_array)
selection_sort_time = measure_time_complexity(selection_sort, random_array)

# Print the results
print("Bubble Sort Time:", bubble_sort_time, "seconds")
print("Insertion Sort Time:", insertion_sort_time, "seconds")
print("Selection Sort Time:", selection_sort_time, "seconds")
