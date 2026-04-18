import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split()) #y = R, x = C
graph = []
for i in range(R):
    graph.append(list(input().rstrip()))

def BFS():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while q:
        s, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if s == "F" and graph[ny][nx] != "#":
                    graph[ny][nx] = "#"
                    q.append(("F", nx, ny))
                elif s == "J" and graph[y][x] != "#" and graph[ny][nx] == ".":
                    graph[ny][nx] = graph[y][x] + 1
                    q.append(("J", nx, ny))
        if s == "J" and x == C - 1 or x == 0 or y == 0 or y == R - 1:
            if graph[y][x] == "#":
                continue
            else:
                print(graph[y][x] + 1)
                exit()

q = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == "F":
            graph[i][j] = "#"
            q.append(("F", j, i))
        if graph[i][j] == "J":
            if j == C - 1 or j == 0 or i == 0 or i == R - 1:
                print(1)
                exit()
            graph[i][j] = 0
            q.appendleft(("J", j, i))

BFS()
print("IMPOSSIBLE")