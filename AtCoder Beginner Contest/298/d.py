import queue
 
Q = int(input())
MOD = 998244353
q = queue.Queue()
q.put(1)
r = 1
for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]
        q.put(x)
        r = (r * 10 + x) % MOD
    elif s[0] == 2:
        y = q.get()
        r = (r - y * pow(10, q.qsize(), MOD)) % MOD
    else:
        print(r)