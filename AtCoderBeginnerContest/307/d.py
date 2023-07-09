import re

def main():
    _ = int(input())
    s = input()

    pattern = re.compile(r'\([^()]*\)')
    while pattern.search(s):
        s = pattern.sub('', s)
    print(s)

main()