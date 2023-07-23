_ = int(input())
S = input()

A = False
B = False
C = False
for i, c in enumerate(S):
    if A and B and C:
        print(i)
        exit(0)
    if c == "A":
        A = True
    if c == "B":
        B = True
    if c == "C":
        C = True
print(i+1)
