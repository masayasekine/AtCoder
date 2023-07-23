import io
import sys
_INPUT = """\
7
6 7 2 1 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
l = list(map(int, input().split()))

N = N + 100
print(N)