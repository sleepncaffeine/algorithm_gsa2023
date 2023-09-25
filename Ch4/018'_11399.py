def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


n = int(input())
arr = list(map(int, input().split()))

arr = insertion_sort(arr)

sum = 0
for i in range(n):
    sum += arr[i] * (n - i)

print(sum)
