# 이전 문제와 마찬가지로 n의 범위가 1000이하이므로 O(n^2)의 시간복잡도까지
# 1초안에 연산할 수 있다. (1초에 1000만번 연산한다고 가정)

# 5 3
# 1 3 2 3 2

# n, m = map(int, input().split())
#
# tmp = map(int, input().split())
# k = [0]
# for i in tmp:
#     k.append(i)
#
# count = 0
# for i in range(1, n):
#     for j in range(i + 1, n + 1):
#         if i == j or k[i] == k[j]:
#             continue
#         print(i, j)
#         count += 1
#
# print(count)

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
print(array)
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)