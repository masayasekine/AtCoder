def main():
    HA, WA = map(int, input().split())
    A = [list(map(str, input().split())) for _ in range(HA)]

    HB, WB = map(int, input().split())
    B = [list(map(str, input().split())) for _ in range(HB)]

    HX, WX = map(int, input().split())
    A = [list(map(str, input().split())) for _ in range(HX)]

    x_sheet = set([])
    for i in range(HA):
        for j in range(HB):
            

main()