def main():
    s = int(input())
    cnt = 0
    for i in range(s):
        a = i+1
        for j in range(s):
            b = j+1
            ab = a * b
            n = s - ab
            for k in range(n):
                c = k+1
                if n % c ==0:
                    d = int(n / c)
                    cd = c * d
                    if ab + cd == s:
                        cnt +=1
                # for l in range(n):
                #     d = l+1
                #     cd = c*d
                #     if ab + cd == s:
                #         cnt += 1

    print(cnt)

main()