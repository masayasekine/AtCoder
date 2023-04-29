def main():
    _ = input()
    S = input()

    count = 0
    counts = []
    left = False
    tmp = ''
    for i, s in enumerate(S):
        if not count:
            if s == '-':
                left = True
        if s == 'o':
            count += 1
        else:
            if count:
                counts.append(count)
            count = 0
    if left and count:
        counts.append(count)
    if not counts:
        print(-1)
        return
    
    print(max(counts))


main()