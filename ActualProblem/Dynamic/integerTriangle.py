# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# https://www.acmicpc.net/problem/1932

n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

#print(tri)

dp = [[-1] * i for i in range(1, n + 1)]

dp[0][0] = tri[0][0]

max_value = 0
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = (dp[i - 1][j] + tri[i][j])

        elif j == i:
            dp[i][j] = (dp[i - 1][j - 1] + tri[i][j])
        else:
            dp[i][j] = (max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j])

        max_value = max(max_value, dp[i][j])

print(max_value)
