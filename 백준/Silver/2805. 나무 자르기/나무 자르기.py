import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
result = 0
cnt_pop = 0
high = 0
for i in range(n):
    k = tree.pop()
    cnt_pop += 1
    if not tree:
        gap = k
    else:
        gap = k - tree[-1]
    result += (gap * cnt_pop)
    
    if result < m:
        continue
    else:
        if not tree:
            high = 0
        else:
            high = tree[-1]
        while True:
            result -= cnt_pop
            if result < m:
                result += cnt_pop
                print(high)
                exit()
                break
            high += 1  