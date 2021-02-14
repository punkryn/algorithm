# N이 1이 될 때까지 수행하는 최소 횟수를 구하는 문제이므로
# 나눗셈을 우선으로 적용하고 안 되면 뺄셈을 적용하는 방법이 횟수를 줄이는 방법이다.

N, K = map(int, input().split())

count = 0

while N != 1:
    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1

print(count)
