arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count = 0
for i in range(1, len(arr)):
    #min_idx = i
    for j in range(i-1, -1, -1):
        print(i, j)
        count += 1
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
        else:
            break

print(count)
print(arr)
