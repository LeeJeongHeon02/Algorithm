n = int(input())
dp = [0] * 1001
dp[1], dp[2], dp[3] = 1, 2, 3
if n <= 3:
    print(dp[n])
for i in range(4, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]
    if n == i:
        print(dp[i] % 10007)