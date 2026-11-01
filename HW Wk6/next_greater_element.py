nums = [2, 1, 2, 4, 3]
ans = [-1] * len(nums)
stack = []
for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]: 
        ans[stack.pop()] = nums[i]
    stack.append(i)
print(ans)

