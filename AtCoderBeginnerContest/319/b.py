import io
import sys
_INPUT = """\
12
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = ""
for i in range(N+1):
    found = False
    for j in range(1,9):
        if i % (N / j) == 0:
            found = True
            ans += str(j)
            break
    if not found:
        ans += "-"
print(ans)

