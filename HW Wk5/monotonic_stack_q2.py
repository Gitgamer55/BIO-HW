arr = list(map(int, input().split()))
stack = []
ans = []

for i in arr:
    while stack and stack[-1] >= i: stack.pop()
    if stack: ans.append(stack[-1])
    else: ans.append(None)
    stack.append(i)

for i in ans: print(i)
