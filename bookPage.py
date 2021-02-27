# 11

# https://www.acmicpc.net/problem/1019

import math

def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0

n = int(input())

#dp = [0] * (n + 1)

num = [0] * 10

# count = 0
# for i in range(1, 11):
#     for j in range(1, 11):
#         if '1' in str(count):
#             print(count, end='  ')
#         else:
#             print(count, end=' ')
#         count += 1
#     print()

length = digit_length(n)

biggest = n // (10 ** (length - 1))

a = 0
zero = 0
for i in range(3, length + 1):
    under = (9 * (10 ** (i - 2))) * (i - 1)
    zero = int(9 * (10 ** (i - 3))) * (i - 2)
    a = int((under - zero) / 9)
    num[0] += zero

    for j in range(1, 10):
        num[j] += a
print(num)


# for i in range(1, biggest):
#     num[i] += 1
#
#     num[0] += zero
#     for j in range(1, 10):
#         num[j] += a
#
# print(num)

def roof(num, index):
    l = int(str(num)[index])
    kkk = length - index
    for i in range(1, l):
        under = (9 * (10 ** (kkk - 2))) * (kkk - 1)
        zero = int(9 * (10 ** (kkk - 3))) * (kkk - 2)
        a = int((under - zero) / 9)
        num[0] += zero
        num[i] += (10 ** (kkk - 1))
        for j in range(1, 10):
            num[j] += (a)