# 7
# 15 11 4 8 5 2 4

# https://www.acmicpc.net/problem/18353

n = int(input())

line = list(map(int, input().split()))

dp = [1] * (n)

line = line[::-1]
#print(line)
for i in range(1, n):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + 1) if line[i] > line[j] else dp[i]

#print(dp)
print(n - max(dp))