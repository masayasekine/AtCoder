S = input()
for i, s in enumerate(S, start=1):
    s = int(s)
    if i >= 2 and i <= 16 and i % 2 == 0:
        if s != 0:
            print("No")
            exit()
print("Yes")
