def main():
    l = list(map(int, input().split()))
    sums = []
    for i in range(l[0] + 1):
        sum_ = 0
        for s in str(i):
            sum_ += int(s)
        if sum_ >= l[1] and sum_ <= l[2]:
            sums.append(i)
    print(sum(sums))

main()