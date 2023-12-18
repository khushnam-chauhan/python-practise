
def reverse(user_input):
    char_stack=[]
    for char in user_input:
        char_stack.append(char)

    reversed=''
    while char_stack:
        reversed=reversed+char_stack.pop()
        
    return reversed
        
original_string = "Hello, World!"
reversed_result = reverse(original_string)

print("Original String:", original_string)
print("Reversed String:", reversed_result)