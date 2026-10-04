stack = []
mapping = {")": "(", "]": "[", "}": "{"}

s = "(]"

for char in s:
    if char in mapping:
        if not stack or mapping[char] != stack.pop():
            print(False)
            break
    else:
        stack.append(char)
else:
    print(len(stack) == 0)
