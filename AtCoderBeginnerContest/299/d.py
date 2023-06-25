def main():
    N = int(input())
    q(1)
    if int(input()) == 1:
        answer(0)
    q(N-1)
    if int(input()) == 0:
        answer(N-1)

    while(i < 18):
        

def q(i: int):
    print(f'? {i}')

def answer(i: int):
    print(f'! {i}')

main()