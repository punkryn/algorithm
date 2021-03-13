n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
for num in lst:
    print(num, end=' ')