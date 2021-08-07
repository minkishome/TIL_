from math import inf

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
coin.sort()

dp = [inf] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

print(dp[-1] if dp[-1] != inf else -1)