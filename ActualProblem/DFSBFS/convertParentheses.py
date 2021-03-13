def solution(p):
    answer = ''

    if p == '':
        return p

    if check(p):
        return p

    point = make_u(p)
    u = p[:point]
    v = p[point:]
    print('u', u)
    print('v', v)

    if check(u):
        #answer += u
        #answer += solution(v)
        u += solution(v)
        return u
    else:
        tmp = ''
        tmp += '('
        tmp += solution(v)
        #tmp += v
        tmp += ')'
        tmp += swap(u[1:-1])
        #answer += tmp
        return tmp
    #return answer

def make_u(p):
    left = 0
    right = 0

    for word in p:
        if word == '(':
            left += 1
        elif word == ')':
            right += 1

        if left == right:
            break

    return left + right

def check(p):
    stack = []
    for i, word in enumerate(p):
        if word == '(':
            stack.append('(')
        elif word == ')':
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True

def swap(p):
    length = len(p)
    tmp = ''
    for i in range(length):
        if p[i] == '(':
            tmp += ')'
        else:
            tmp += '('

    # print('tmp', tmp)
    return tmp

plist = ['((())))(', "()))((()", ')(())(', ')(', '()))((()', ')()(()(()))(', ')))(((()']
p = "()))((()"

for p in plist:
    print(solution(p))