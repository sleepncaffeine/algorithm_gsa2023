def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        print(f"step {i:02d}: ", arr)
    return arr


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
selection_sort(arr)
print("정렬 후: ", arr)
