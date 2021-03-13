# 11

# https://www.acmicpc.net/problem/1019

from sys import stdin

def calc(n, point):
    while n > 0:
        ans[n % 10] += point
        n = n // 10

n = int(stdin.readline())

ans = [0] * 10

# def solution(a, b, count):
#     #print('a, b', a, b)
#     if a > b:
#         return
#     else:
#         while b % 10 != 9 and a <= b:
#             calc(b, count)
#             b -= 1
#
#         while a % 10 != 0 and a <= b:
#             calc(a, count)
#             a += 1
#
#         if a == b:
#             return
#
#         for i in range(10):
#             ans[i] += ((b // 10) - (a // 10) + 1) * (10 ** (count - 1))
#
#         solution(a // 10, b // 10, count + 1)
#
# # tmp = 0
# # ctmp = 1
# # zero = 0
# # for _ in range(len(str(n)) - 1):
# #     ans[0] += tmp
# #     for i in range(1, 10):
# #         ans[i] += (ctmp + tmp * 9)
# #
# #     tmp = (ctmp + tmp * 9)
# #     ctmp *= 10
#
# #solution(10 ** (len(str(n)) - 1), n, 1)
# solution(1, n, 1)
#
# for i in range(10):
#     print(ans[i], end=' ')

point = 1
start = 1

while(start <= n):
    #print(start, n)
    while(n % 10 != 9 and start <= n):
        calc(n, point)
        n -= 1
    #print('n',n)
    if n < start:
        break

    while start % 10 != 0 and start <= n:
        calc(start, point)
        start += 1
    #print('start', start)
    start //= 10
    n //= 10
    #print(n, start)
    #print((n - start + 1) * point)
    for i in range(10):
        ans[i] += ((n - start + 1) * point)

    point *= 10

for i in range(10):
    print(ans[i], end=' ')