MAX_SIZE = 100  # Maximum size of the stack
stack = []
top = -1  # Index of the top element in the stack

def push(item):
    global top
    if top < MAX_SIZE - 1:
        top += 1
        stack.append(item)
    else:
        print("Stack overflow. Cannot push to a full stack.")

def pop():
    global top
    if top >= 0:
        top -= 1
        return stack.pop()
    else:
        print("Stack is empty. Cannot pop from an empty stack.")
        return None
push(1)
push(2)
push(3)

print("Stack after push operations:", stack)

print("Popped item:", pop())
print("Stack after pop operation:", stack)