n, m = map(int, input().split())

nList = []
for _ in range(n):
    nList.append(int(input()))

d = [10001] * (m+1)

# for item in nList:
#     d[item] = 1
#
# d[m] = -1
#
# for i in range(min(nList), m+1):
#     tmp = []
#     for k in nList:
#         a = d[i - k]
#         #print(a)
#         if a != 0:
#             tmp.append(d[i - k] + 1)
#     try:
#         d[i] = min(tmp)
#     except ValueError:
#         pass
#
# print(d)
# print(d[m])

d[0] = 0
for i in range(n):
    for j in range(nList[i], m+1):
        if d[j - nList[i]] != 10001:
            d[j] = min(d[j], d[j - nList[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])