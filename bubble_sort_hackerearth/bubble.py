n = int(input())
arr = list(map(int, input().split()))
count = 0
swapped = True
while swapped:
    count += 1
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            swapped = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(count)
