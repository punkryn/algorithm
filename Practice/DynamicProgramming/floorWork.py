n = int(input())

arr = [0] * (n+1)
# result = 0
# if n % 2 == 1:
#     for i in range(n+1):
#         if i % 2 == 0:
#             continue
#         if i == 1:
#             arr[i] = (2 ** ((n - i)//2)) * ((n+1)//2)
#             print(arr[i])
#             result += arr[i]
#         elif i < n:
#             arr[i] = (i+1) * (2 ** ((n-i)//2))
#             result += arr[i]
#         elif i == n:
#             arr[i] = 1
#             result += arr[i]
#
# print(arr)
# print(result)
#

arr[1] = 1
arr[2] = 3
for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2]*2) % 769769

print(arr)
print(arr[n])
