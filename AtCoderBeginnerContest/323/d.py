# これはTLEする

N = int(input())
# スライムのサイズと引数の対応を辞書型で保持
slime = {}
for i in range(N):
    a, b = map(int, input().split())
    slime[a] = b

# 2n匹のスライムを合成して倍のサイズのスライムをn匹追加する関数
def merge(slime, key):
    if slime.get(key*2) is None:
        slime[key*2] = 0
    slime[key*2] = slime[key*2] + slime[key] // 2
    slime[key] = slime[key] - (slime[key] // 2) * 2
    return slime

# スライムの合成が可能かどうかを判定する関数
def check(slime):
    for key in slime.keys():
        if slime[key] >= 2:
            return True
    return False

while check(slime):
    # サイズが小さい順にスライムを合成する
    for key in sorted(slime.keys()):
        if slime[key] >= 2:
            slime = merge(slime, key)
            break

print(sum(slime.values()))
