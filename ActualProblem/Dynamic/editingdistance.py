# sunday
# saturday

a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

n = len(a)
m = len(b)
for i in range(1, n + 1):
    dp[i][0] = i

for j in range(1, m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

for i in range(n + 1):
    for j in range(m + 1):
        print(dp[i][j], end=' ')
    print()
print()

print(dp[n][m])