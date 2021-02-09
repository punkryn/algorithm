# 주어진 문자열에서 첫 번째 자리가 0 또는 1인 경우엔 더하기를 수행하고
# 그 외의 경우에는 곱하기를 수행한다.

# 02984
# 567

num = input()

result = 0
pre = num[0]
for i in range(1, len(num)):
    #print(pre, num[i])
    if pre == '0' or pre == '1':
        if i == 1:
            result += int(pre)
        result = int(num[i]) + result
    else:
        if i == 1:
            result += int(pre)
        result = int(num[i]) * result

    pre = num[i]

print(result)