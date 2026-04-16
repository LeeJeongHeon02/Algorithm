import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split()) # W = x, H = y
visit = [[[-1] * W for _ in range(H)] for _ in range(K + 1)]
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

x_monkey = [0, 1, 0, -1]
y_monkey = [-1, 0, 1, 0]
x_horse = [1, 2, 2, 1, -1, -2, -2, -1]
y_horse = [2, 1, -1, -2, -2, -1, 1, 2]
def BFS():
    q = deque()
    q.append((0, 0, K)) # x, y, K
    visit[0][0][0] = 0
    while q:
        x, y, k = q.popleft()
        if x == W - 1 and y == H - 1:
            print(visit[k][y][x] + 1)
            return
        for i in range(4):
            nx = x + x_monkey[i]
            ny = y + y_monkey[i]
            if 0 <= nx < W and 0 <= ny < H:
                if visit[k][ny][nx] == -1 and graph[ny][nx] == 0:
                    visit[k][ny][nx] = visit[k][y][x] + 1
                    q.append((nx, ny, k))
        if k > 0:
            for j in range(8):
                nx = x + x_horse[j]
                ny = y + y_horse[j]
                if 0 <= nx < W and 0 <= ny < H:
                    if visit[k - 1][ny][nx] == -1 and graph[ny][nx] == 0:
                        visit[k - 1][ny][nx] = visit[k][y][x] + 1
                        q.append((nx, ny, k - 1))
    print(-1)
BFS()