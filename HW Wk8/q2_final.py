memo = {}

def dp(amount, coins):
    if amount in memo: return memo[amount]
    if amount < 0: return float('inf')
    if amount == 0: return 0
    sum = float('inf')
    for coin in coins: sum = min(sum, dp(amount-coin, coins) + 1)
    memo[amount] = sum
    return sum


lst = list(map(int, input().split()))
target = int(input())
dp(target, lst)
print(memo[target] if memo[target] != float('inf') else -1)
