def main():
    #空のリスト
    A = []
    #リストAにappend()を使って格納していく
    for _ in range(8):
        A.append(str(input()))
    
    alp = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    
    for i, S in enumerate(A, start=1):
        for j, s in enumerate(S, start=1):
            if s == '*':
                print(alp[j]+str(9 - i))


main()