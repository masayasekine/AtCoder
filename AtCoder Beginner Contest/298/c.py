import bisect

def main():
    _ = int(input())
    Q = int(input())
    quries = [list(map(int, input().split())) for l in range(Q)]

    # 箱
    boxies = {}
    # 数字がどの箱に入っているか管理する
    num_box = {}

    for q in quries:
        if q[0] == 1:
            if q[2] not in boxies.keys():
                boxies[q[2]] = [q[1]]
            else:
                bisect.insort_right(boxies[q[2]], q[1])
            if q[1] not in num_box.keys():
                num_box[q[1]] = [q[2]]
            else:
                if q[2] not in num_box[q[1]]:
                    bisect.insort_right(num_box[q[1]], q[2])
            continue
        if q[0] == 2:
            print(*boxies[q[1]])
            continue
        if q[0] == 3:
            print(*num_box[q[1]])

main()
