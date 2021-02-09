# 왼쪽에서부터 연속한 숫자를 세어서 연속한 숫자의 그룹이 적은 수를
# 뒤집는 횟수로 한다. 예를 들어 0그룹이 2개 1그룹이 1개면
# 1그룹을 뒤집으면 되기 때문에 뒤집는 횟수를 1로 한다.

# 0001100

string = input()

index = 0
zero_count = 0
one_count = 0
while index < len(string) - 1:
    now = string[index]
    next = string[index + 1]
    #print(now, next)
    if now == next:
        index += 1
    else:
        index += 1
        if now == '0':
            zero_count += 1
            #print('now', now, index)
        else:
            one_count += 1
            #print('now', now, index)

if string[index] == '0':
    zero_count += 1
else:
    one_count += 1

print(min(zero_count, one_count))