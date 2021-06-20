a = [0] * 3
i = 0
a[0] = 2
a[1] = 4
def q(B):
    global i
    a[i] = 3
    i = 1
    print(B)

q(a[i])
