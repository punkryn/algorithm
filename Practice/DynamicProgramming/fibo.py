d = [0] * 100

def fibo(x):
    if x == 0 or x == 1:
        return 1
    elif d[x] != 0:
        return d[x]
    else:
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

print(fibo(6))