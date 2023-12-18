def user_defined_sort(input_list):
    """
    This function sorts the given list using the bubble sort algorithm.
    """
    n = len(input_list)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
user_defined_sort(my_list)
print("Sorted List:", my_list)
