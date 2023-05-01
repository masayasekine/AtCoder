from collections import deque
def main():
    H, W = map(int, input().split())
    A = [list(map(str, input().split())) for _ in range(H)]
    B = [list(map(str, input().split())) for _ in range(H)]
    
    A_ = deque(A)
    B_ = deque(B)
    for _ in range(H):
        for i in range(W):
            for j in range (H):
                d = deque(A_[j][0])
                d.rotate(-1)
                A_[j][0] = ''.join(list(d))
            if A_ == B_:
                print('Yes')
                return
        A_.rotate(-1)
    print('No')

main()