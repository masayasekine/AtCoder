_ = int(input())
S = input()

befor = S[:len(S)//2]
after = S[len(S)//2:]

if befor == after:
    print('Yes')
else:
    print('No')