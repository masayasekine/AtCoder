A, B = map(int, input().split())
if A == 1:
    print('Yes') if B == 2 else print('No')
if A == 2:
    print('Yes') if B == 1 or B == 3 else print('No')
if A == 3:
    print('Yes') if B == 2 else print('No')
if A == 4:
    print('Yes') if B == 5 else print('No')
if A == 5:
    print('Yes') if B == 4 or B == 6 else print('No')
if A == 6:
    print('Yes') if B == 5 else print('No')
if A == 7:
    print('Yes') if B == 8 else print('No')
if A == 8:
    print('Yes') if B == 7 or B == 9 else print('No')

