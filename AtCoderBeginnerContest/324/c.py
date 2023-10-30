def check(target, original):
    # originalとtargetが同一
    if target == original:
        return True
    
    target_len = len(target)
    original_len = len(original)
    # targetはoriginalのいずれか1つの位置（先頭と末尾も含む）に英小文字を1つ挿入して得られる文字列である。
    if target_len == original_len + 1:
        for i in range(target_len):
            if target[:i] + target[i+1:] == original:
                return True
    # targetはoriginalからある1文字を取り除いて得られる文字列である。
    if target_len == original_len - 1:
        for i in range(original_len):
            if original[:i] + original[i+1:] == target:
                return True
    # targetはoriginalのある1文字を任意の英小文字に置き換えて得られる文字列である。
    if target_len == original_len:
        for i in range(original_len):
            if original[:i] + target[i] + original[i+1:] == target:
                return True

l = list(map(str, input().split()))
N = int(l[0])
original = l[1]
targets = [input() for _ in range(N)]

ans = []
for i, target in enumerate(targets):
    if check(target, original):
        ans.append(i+1)
print(len(ans))
print(*ans)