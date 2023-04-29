def main():
    _ = int(input())
    S = input()
    pipe_left = False
    pipe_right = False
    target = False
    for s in S:
        if s == '|':
            if not pipe_left:
                pipe_left = True
            else:
                if target:
                    print('in')
                else:
                    print('out')
                return
        elif s == '*':
            if not pipe_left:
                print('out')
                return
            target = True

main()