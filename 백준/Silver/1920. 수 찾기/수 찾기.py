import sys

n = int(sys.stdin.readline())
a1 = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
a2 = list(map(int, sys.stdin.readline().split()))

for i in a2:
    if i in a1:
        print(1)
    else:
        print(0)