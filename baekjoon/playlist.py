# https://www.acmicpc.net/problem/12872
# https://sgc109.tistory.com/66

MOD = int(1e9 + 7)

n, m, p = map(int, input().split())

dp = [[0] * 101 for _ in range(101)]

dp[0][0] = 1

for i in range(p + 1):
    for j in range(n + 1):
        if j > 0:
            dp[i][j] += dp[i-1][j-1] * (n - j + 1)
            dp[i][j] %= MOD

        if j > m:
            dp[i][j] += dp[i-1][j] * (j-m)
            dp[i][j] %= MOD

print(dp[p][n])
