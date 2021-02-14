# m이 1만 이하일 때는 시간초과가 뜨지 않음

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
count = 0
result = 0
for i in range(M):
    if count == K:
        result += data[1]
        count = 0
        continue

    result += data[0]
    count += 1

print(result)

#m이 100억 정도 되면? 정렬없이 수학적으로 푸는 법

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(int(M/(K+1)) * (data[0] * K + data[1]) + M % (K+1) * data[0])