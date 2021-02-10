# https://programmers.co.kr/learn/courses/30/lessons/60057
# ababcdcdababcdcd

def solution(s):
    answer = 0

    length = len(s)

    count = 1
    result = []
    sw = 0
    for i in range(1, length // 2 + 1):
        tmp = ''
        pre = 0
        # for j in range(0, length - i):
        j = 0
        count = 1
        sw = 0
        while j < length - i:
            # print(s[j:j + i], s[j + i:j + i + i])
            #print(j, i)
            #print(s[j:j + i], s[j + i:j + i + i])
            if s[j:j + i] == s[j + i:j + i + i]:
                pre = count
                count += 1
                j += i
                sw = 1
            else:
                if sw == 1:
                    tmp += ((str)(count if count != 1 else '') + s[j: j + i])
                elif sw == 2:
                    tmp += ((str)(count if count != 1 else '') + s[j])
                # print(tmp)

                count = 1
                if sw == 1:
                    j += i
                elif sw == 2:
                    j += 1
                sw = 2
        if sw == 1:
            tmp += ((str)(count if count != 1 else '') + s[j: j + i])
        elif sw == 2:
            tmp += s[j:]
        print(tmp)
        result.append(len(tmp)) if  len(tmp) > 0 else 1
    print(result)
    answer = min(result)
    return answer

s = '123'
print(s[2:3])

s = input()

print(solution(s))