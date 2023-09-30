K = int(input())
k = 0

for q in range(10):
    for w in range(10):
        if q and q <= w:
            continue
        for e in range(10):
            if (q or w) and w <= e:
                continue
            for r in range(10):
                if (q or w or e) and e <= r:
                    continue
                for t in range(10):
                    if (q or w or e or r) and r <= t:
                        continue
                    for y in range(10):
                        if (q or w or e or r or t) and t <= y:
                            continue
                        for u in range(10):
                            if (q or w or e or r or t or y) and y <= u:
                                continue
                            for i in range(10):
                                if (q or w or e or r or t or y or u) and u <= i:
                                    continue
                                for o in range(10):
                                    if (q or w or e or r or t or y or u or i) and i <= o:
                                        continue
                                    for p in range(10):
                                        if (q or w or e or r or t or y or u or i or o) and o <= p:
                                            continue
                                        k += 1
                                        if k == K + 1:
                                            print(int(str(q) + str(w) + str(e) + str(r) + str(t) + str(y) + str(u) + str(i) + str(o) + str(p)))
                                            exit(0)