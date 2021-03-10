# 5 4
# 1 3 5 6 10
#
# 5 3
# 1 3 5 5 5

# 10 5
# 1 2 2 2 3 4 4 5 5 5

# https://www.acmicpc.net/problem/13164

n, k = map(int, input().split())

heights = list(map(int, input().split()))

diff = []
for i in range(n - 1):
    diff.append(heights[i + 1] - heights[i])

diff.sort()

sum = 0
for i in range(n - k):
    sum += diff[i]

print(sum)

# index = list(range(1, len(heights)))
# group = []
# result = 0
# for _ in range(k-1):
#     dis = int(1e9)
#     minimum_index = -1
#     for i in index:
#         group.append(i)
#         group.sort()
#
#         comp = 0
#         comp += (heights[group[0] - 1] - heights[0])
#         for j in range(len(group) - 1):
#             comp += (heights[group[j+1] - 1] - heights[group[j]])
#
#         comp += (heights[-1] - heights[group[-1]])
#
#         if dis > comp:
#             minimum_index = i
#             dis = comp
#
#         group.remove(i)
#
#     #result = dis
#     group.append(minimum_index)
#     index.remove(minimum_index)
#
# # print(group)
#
# #result = 0
# if group:
#     group.sort()
#     result += (heights[group[0] - 1] - heights[0])
#     for j in range(len(group) - 1):
#         result += (heights[group[j+1] - 1] - heights[group[j]])
#
#     result += (heights[-1] - heights[group[-1]])
#
# print(result)

