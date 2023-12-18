def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        # Handle the specific exception (division by zero)
        print(f"Error: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
    else:
        # Executed if no exception occurs
        print(f"The result of {a} / {b} is {result}")
    finally:
        # Executed regardless of whether an exception occurred
        print("Finally block executed")

# Test the function with different inputs
divide_numbers(10, 2)   # No exception
divide_numbers(10, 0)   # Raises a ZeroDivisionError
divide_numbers("10", 2)  # Raises a TypeError
