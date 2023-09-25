from collections import deque


def radix_sort(arr):
    buckets = [deque() for _ in range(10)]
    queue = deque(arr)
    exp = 1
    max_num = max(arr)

    while max_num >= exp:
        while queue:
            num = queue.popleft()
            buckets[(num // exp) % 10].append(num)

        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())

        exp *= 10

    return list(queue)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전: ", arr)
arr = radix_sort(arr)
print("정렬 후: ", arr)
