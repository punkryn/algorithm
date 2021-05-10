INF = int(1e9)
def DPCoinChange(change, coin):
    k = len(coin)
    C = [INF] * (change + 1)
    C[0] = 0

    for j in range(1, change + 1):
        for i in range(k):
            if coin[i] <= j and (C[j - coin[i]] + 1 < C[j]):
                C[j] = C[j - coin[i]] + 1

    print(C)
    return C[-1]

coin = [1, 5, 10, 16]
change = 31

print(DPCoinChange(change, coin))