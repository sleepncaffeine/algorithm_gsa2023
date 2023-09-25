def merge_sort(arr, s, e):
    if s < e:
        m = (s + e) // 2
        merge_sort(arr, s, m)
        merge_sort(arr, m + 1, e)
        merge(arr, s, m, e)


def merge(arr, s, m, e):
    n1 = m - s + 1
    n2 = e - m
    L = [arr[s + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]

    i, j, k = 0, 0, s
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = L[j]
        k += 1
        j += 1


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
merge_sort(arr, 0, len(arr) - 1)
print("정렬 후: ", arr)
