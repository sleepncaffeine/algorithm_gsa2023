# 009
# boj 12891

import collections

s, p = map(int, input().split())
dna = list(input())
min_cnt = list(map(int, input().split()))

# 부분문자열에 포함되어야 할 ACGT의 개수를 dict로
dna_char = "ACGT"
need_cnt = dict()
for i in range(4):
    need_cnt[dna_char[i]] = min_cnt[i]
current_cnt = collections.Counter(dna[:p])


def check() -> int:  # 0/1
    for c in dna_char:
        if current_cnt[c] < need_cnt[c]:
            return 0
    return 1


pwd = 0
pwd += check()

for i in range(s - p):
    current_cnt[dna[i]] -= 1
    current_cnt[dna[i + p]] += 1
    pwd += check()

print(pwd)
