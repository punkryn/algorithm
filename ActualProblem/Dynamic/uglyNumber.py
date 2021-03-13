n = int(input())

# numlist =[1, 2, 3, 4, 5]
#
# count = 5
# i = 6
# while count < n:
#     #print(i)
#     if i % 2 == 0:
#         if (i / 2) in numlist:
#             numlist.append(i)
#             count += 1
#     elif i % 3 == 0:
#         if (i / 3) in numlist:
#             numlist.append(i)
#             count += 1
#     elif i % 5 == 0:
#         if (i / 5) in numlist:
#             numlist.append(i)
#             count += 1
#     i += 1
#
# # print(numlist)
# if n <= 5:
#     print(numlist[n-1])
# else:
#     print(numlist[-1])

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)

    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])