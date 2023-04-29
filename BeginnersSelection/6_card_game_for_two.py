def main():
    _ = int(input())
    l = list(map(int, input().split()))

    sorted_l = sorted(l, reverse=True)

    alice = []
    bob = []
    for i, n in enumerate(sorted_l):
        if i % 2 == 0:
            alice.append(n)
        else:
            bob.append(n)
    print(sum(alice) - sum(bob))

main()