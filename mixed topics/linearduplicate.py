def find_duplicates(input_list):
    """
    This function finds and prints all duplicate elements in the given list using linear search.
    """
    n = len(input_list)
    duplicates = []

    for i in range(n):
        for j in range(i + 1, n):
            if input_list[i] == input_list[j] and input_list[i] not in duplicates:
                duplicates.append(input_list[i])

    if duplicates:
        print("Duplicate elements:", duplicates)
    else:
        print("No duplicate elements found.")

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 9, 9]
find_duplicates(my_list)
