change = int(input())

n500 = n170 = n100 = n50 = n10 = n1 = 0

if change >= 500:
    n500 = change // 500
    change %= 500

if change >= 170:
    n170 = change // 170
    change %= 170

if change >= 100:
    n100 = change // 100
    change %= 100

if change >= 50:
    n50 = change // 50
    change %= 50

if change >= 10:
    n10 = change // 10
    change %= 10

n1 = change // 1

print(n500, n170, n100, n50, n10, n1)
print(n500 + n170 + n100 + n50 + n10 + n1)
