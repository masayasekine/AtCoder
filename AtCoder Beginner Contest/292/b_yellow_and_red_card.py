def card():
    N, Q = map(int, input().split())
    l = [list(map(int, input().split())) for l in range(Q)]
    players = {}
    for i in range(N):
        players[i+1] = 0
    for event in l:
        if event[0] == 1:
            players[event[1]] += 1
        elif event[0] == 2:
            players[event[1]] += 2
        elif event[0] == 3:
            print('Yes') if players[event[1]] >= 2 else print('No')

card()