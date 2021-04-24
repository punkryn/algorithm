# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    return str(int(''.join(numbers)))

numbers = [3, 30, 3433, 0, 5, 50, 9, 99]
#numbers = [90,908,89,898,10,101,1,8,9]

print(solution(numbers))