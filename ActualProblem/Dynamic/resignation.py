# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# 2 20
# 3 30
# 4 40
# 5 50

# https://www.acmicpc.net/problem/14501

n = int(input())

week = [list(map(int, input().split())) for _ in range(n)]

#print(week)

money = [0] * (n + 1)
max_value = 0
for i in range(n - 1, -1, -1):
    day, pay = week[i]
    #print('day, i', day, i)
    if day + i > n:
        money[i] = max_value
    elif day + i == n:
        money[i] = max(money[day + i] + pay, max_value)
        max_value = money[i]
    else:
        # if money[day + i] != 0:
        money[i] = max(money[day + i] + pay, max_value)
        max_value = money[i]
        # else:
        #     money[i] = pay

    #print(week)
    #print(money)

print(max(money))


# n = int(input())
# t = []
# p = []
# dp = [0] * (n + 1)
# max_value = 0
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     t.append(x)
#     p.append(y)
#
# for i in range(n - 1, -1, -1):
#     print(dp)
#     time = t[i] + i
#
#     if time <= n:
#         dp[i] = max(p[i] + dp[time], max_value)
#         max_value = dp[i]
#
#     else:
#         dp[i] = max_value
#
# print(dp)
# print(max_value)