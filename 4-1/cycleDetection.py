graph = [[6], [6], [0], [1], [4], [3], [3], [4], [0]]

slow = graph[2][0]
fast = graph[graph[2][0]][0]
#print(slow, fast)

loop = False
while slow != fast:
    slow = graph[slow][0]
    fast = graph[graph[fast][0]][0]

    #print(slow ,fast)

    if slow == fast:
        loop = True
        break

length = 0
if loop:
    slow = graph[2][0]
    fast = graph[fast][0]
    while True:
        slow = graph[slow][0]
        fast = graph[fast][0]

        length += 1
        if slow == fast:
            break

print(fast, slow)