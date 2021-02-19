# 가장 인접한 두 집 사이의 거리 차가 최대가 되는 집을 탐색하는 것
# 두 집 사이의 거리는 1 ~ 8, 이 범위에서 이분탐색을 진행하며
# 공유기를 3개 설치할 수 있는지 찾는다.

# 5 3
# 1
# 2
# 8
# 4
# 9

# https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())

home = [int(input()) for _ in range(n)]

home.sort()

start = home[1] - home[0]
end = home[-1] - home[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    value = home[0]
    for i in range(1, n):
        if home[i] >= mid + value:
            value = home[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)