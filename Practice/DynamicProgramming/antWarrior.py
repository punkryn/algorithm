n = int(input())

k = list(map(int, input().split()))

# O(N^2)
# result = 0
# for i in range(len(k)):
#     count = 0
#     pre = i
#     for j in range(len(k)):
#         if i - j == 1 or i - j == -1 or pre - j == 1 or pre - j == -1:
#             continue
#
#         pre = j
#         count += k[j]
#
#     if result < count:
#         result = count
#
# print(result)

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])
