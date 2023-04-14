def main():
    s = input()
    k = 0
    left_r = 0
    right_r = 0
    left_b = 0
    right_b = 0
    
    for i, c in enumerate(s, start=1):
        if c == 'K':
            if left_r == 0:
                print('No')
                return
            if right_r != 0:
                print('No')
                return
            k = i
        if c == 'R':
            if left_r == 0:
                if k != 0:
                    print('No')
                    return
                left_r = i
                continue
            right_r = i
        if c == 'B':
            if left_b == 0:
                left_b = i
                continue
            right_b = i
    left_odd = left_b % 2 == 0
    right_odd = right_b % 2 == 0
    if left_odd == right_odd:
        print('No')
        return
    print('Yes')
    return

main()