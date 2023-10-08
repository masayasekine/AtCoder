import io
import sys
_INPUT = """\
3
3 3
5 1
6 1
"""
sys.stdin = io.StringIO(_INPUT)

from heapq import heapify, heappop, heappush
from sys import stdin

input = stdin.readline
n = int(input())
heap = [tuple(map(int, input().split())) for _ in range(n)]

heapify(heap)

ans = 0
while heap:
    s, c = heappop(heap)
    while heap and heap[0][0] == s:
        c += heappop(heap)[1]
    if c >= 2:
        heappush(heap, (2 * s, c // 2))
    ans += c % 2

print(ans)