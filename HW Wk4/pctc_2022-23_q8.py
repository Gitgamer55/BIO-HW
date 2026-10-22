s = input()
stack = []
result = []
for char in s:
    if char == '[':
        stack.append([])
    elif char.isdigit():
        stack[-1].append(int(char))
    elif char == ']':
        current = stack.pop()
            
        first = current[0]
        last = current[-1]

        avg = (first + last) // 2
        result.append(str(avg))
            
print("".join(result))
