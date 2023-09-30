N = int(input())
A = []
total_z = 0
win_z = 0
for i in range(N):
    X, Y, Z = map(int, input().split())
    if X > Y:
        win_z += Z
    else:
        cost = (Y - X) // 2 + 1
        score = Z / cost
        A.append([X, Y, Z, cost, score])
    total_z += Z

if win_z > total_z // 2:
    print(0)
    exit(0)

sorted_A = sorted(A, key=lambda x: x[4], reverse=True)
ans = 0
for a in sorted_A:
    ans += a[3]
    win_z += a[2]
    if win_z > total_z / 2:
        print(ans)
        exit(0)

