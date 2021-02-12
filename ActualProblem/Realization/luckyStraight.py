# 123402
# https://acmicpc.net/problem/18406



def cal(n):
    length = len(n)
    left = n[:(length//2)]
    right = n[(length//2):]

    left_result = 0
    right_result = 0

    for i in range(len(left)):
        left_result += int(left[i])
        right_result += int(right[i])

    #print(left_result, right_result)
    if left_result == right_result:
        print('LUCKY')
    else:
        print('READY')

n = (input())

cal(n)