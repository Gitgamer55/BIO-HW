s = input()
stack = []
for char in s:
    if char == '(':
        stack.append('(')
    elif char.isdigit():
        val = int(char)
        if stack and isinstance(stack[-1], int):
            a = stack.pop()
            b = val
            stack.append(a * b + a + b)
        else:
            stack.append(val)
    elif char == ')':
        val = stack.pop()
        stack.pop() 
        if stack and isinstance(stack[-1], int):
            a = stack.pop()
            b = val
            stack.append(a * b + a + b)
        else:
            stack.append(val)
print(stack[0])
