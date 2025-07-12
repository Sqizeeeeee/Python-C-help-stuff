from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(f'{stack.pop()} popped from stack')
print(f'Top element is: {stack[-1]}' if stack else 'Stack is empty')