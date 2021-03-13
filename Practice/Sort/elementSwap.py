n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    for j in range(i+1):
        if a[i] < b[j]:
            a[i], b[j] = b[j], a[i]

result = 0
for j in range(n):
    result += a[j]

print(a)
print(b)
print(result)