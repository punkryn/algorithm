# N의 범위가 1000이하일 때 시간복잡도 O(N^2) 정도의 알고리즘은
# 100만번의 연산을 수행하기 때문에 제한 시간인 1초 안에 충분히 가능하다.
# 따라서 2중 반복문을 사용하여도 괜찮다.

# 5
# 3 2 1 1 9

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
    print(target, x)

# 만들 수 없는 금액 출력
print(target)
