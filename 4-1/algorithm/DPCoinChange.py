INF = int(1e9)
def DPCoinChange(change, coin):
    k = len(coin)
    C = [INF] * (change + 1)
    C[0] = 0

    coin_type = [{}] * (change + 1)

    for j in range(1, change + 1):
        for i in range(k):
            if coin[i] <= j and (C[j - coin[i]] + 1 < C[j]):
                C[j] = C[j - coin[i]] + 1

        minimum = min(coin, key=lambda x: C[j - x] + 1 if j >= x else INF)

        if minimum not in coin_type[j - minimum].keys():
            tmp = coin_type[j - minimum].copy()
            tmp[minimum] = 1
            coin_type[j] = tmp
        else:
            tmp = coin_type[j - minimum].copy()
            tmp[minimum] += 1
            coin_type[j] = tmp

    print(coin_type)
    print(C)
    return C, coin_type

coin = [1, 5, 10, 16]
change = 25

C, coin_type = DPCoinChange(change, coin)
print(coin_type[25])

for i in range(1, 26):
    print("거스름돈: " + str(i) + "원")
    for key in coin_type[i].keys():
        print(str(key)+"원짜리 동전 " + str(coin_type[i][key]) +"개")
    print()