def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"step {i:02d}: ", arr)
    return arr


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
insertion_sort(arr)
print("정렬 후: ", arr)
