# https://www.acmicpc.net/problem/5585

# 380

n = int(input())

change = 1000 - n

count = 0

changelist = [500, 100, 50, 10, 5, 1]

for i in range(6):
    if change >= changelist[i]:
        count += (change // changelist[i])
        change %= changelist[i]

print(count)
