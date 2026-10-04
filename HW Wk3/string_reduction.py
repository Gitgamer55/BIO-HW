def pair(s1, s2):
    return abs(ord(s1) - ord(s2)) % 24 == 1


stack = []
s = "adcb"

for char in s:
    if stack and pair(char, stack[-1]):
        stack.pop()
    else:
        stack.append(char)

print("".join(stack))