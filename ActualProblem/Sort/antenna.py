# 4
# 5 1 7 9

# 5
# 1 5 9 10 15

# https://www.acmicpc.net/problem/18310

n = int(input())

num = list(map(int, input().split()))

num.sort()

print(num[(n-1)//2])