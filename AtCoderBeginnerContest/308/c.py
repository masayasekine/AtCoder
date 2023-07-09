from decimal import Decimal
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    ps = []
    for i, a in enumerate(A, start=1):
        head = Decimal(a[0])
        tail = Decimal(a[1])
        p = head / (head + tail)
        ps.append([p, i])
    ps.sort(key=lambda x: (-x[0], x[1]))

    ans = []
    for p in ps:
        ans.append(p[1])
    print(*ans)

main()
