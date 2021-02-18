# 3
# 10
# 20
# 40

# 1
# 10

# 2
# 20
# 10

# https://acmicpc.net/problem/1715

import heapq

n = int(input())

deck = []

for i in range(n):
    heapq.heappush(deck, int(input()))

result = 0

# if len(deck) == 1:
#     result = heapq.heappop(deck)
# else:
#     while deck:
#         a = heapq.heappop(deck)
#         b = heapq.heappop(deck)
#
#
#         result += (a + b)
#
#         if deck:
#             heapq.heappush(deck, (a + b))

while len(deck) != 1:
    one = heapq.heappop(deck)
    two = heapq.heappop(deck)

    sum_value = one + two

    result += sum_value
    heapq.heappush(deck, sum_value)

print(result)