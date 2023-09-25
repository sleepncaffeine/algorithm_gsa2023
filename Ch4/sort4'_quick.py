def quick_sort(arr, s, e):
    if s >= e:
        return
    p = partition(arr, s, e)
    quick_sort(arr, s, p - 1)
    quick_sort(arr, p, e)


def partition(arr, s, e):
    mid = (s + e) // 2
    pivot = arr[mid]

    while s <= e:
        while arr[s] < pivot:
            s += 1
        while arr[e] > pivot:
            e -= 1
        if s <= e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

    return s


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
quick_sort(arr, 0, len(arr) - 1)
print("정렬 후: ", arr)
