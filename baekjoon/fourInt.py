# https://acmicpc.net/problem/7453

# 6
# -45 22 42 -16
# -41 -27 56 30
# -36 53 -37 77
# -36 30 -75 -46
# 26 -38 -10 62
# -32 -54 -6 45

# 1
# 1 -1 -3 3

# from sys import stdin
#
# n = int(stdin.readline())
#
# a = []
# b = []
# c = []
# d = []
#
# for _ in range(n):
#     a1, b1, c1, d1 = map(int, stdin.readline().split())
#     a.append(a1)
#     b.append(b1)
#     c.append(c1)
#     d.append(d1)
#
# ab = {}
# for i in range(n):
#     for j in range(n):
#         if not ab.get(a[i] + b[j]):
#             ab[a[i] + b[j]] = 1
#         else:
#             ab[a[i] + b[j]] += 1
#
# cd = {}
# for i in range(n):
#     for j in range(n):
#         if not cd.get(c[i] + d[j]):
#             cd[c[i] + d[j]] = 1
#         else:
#             cd[c[i] + d[j]] += 1
#
# #print(ab)
# #print(cd)
#
# count = 0
# for _, key in enumerate(ab):
#     if cd.get(-key):
#         count += (ab[key] * cd[-key])
#
# print(count)


from sys import stdin



n = int(input())
array = [list(map(int, stdin.readline().split())) for _ in range(n)]

a_list, b_list, c_list, d_list = list(), list(), list(), list()
for i in range(n):
    for j in range(4):
        value = array[i][j]
        if j == 0:
            a_list.append(value)
        elif j == 1:
            b_list.append(value)
        elif j == 2:
            c_list.append(value)
        elif j == 3:
            d_list.append(value)

ab = dict()

# ab 가능한 합 계산
for a in a_list:
    for b in b_list:
        ab[a + b] = ab.get(a + b, 0) + 1

# cd 가능한 합 계산
answer = 0
for c in c_list:
    for d in d_list:
        answer += ab.get(-(c + d), 0)

print(answer)