# 015
# boj 2750

import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(f"{i}\n")
