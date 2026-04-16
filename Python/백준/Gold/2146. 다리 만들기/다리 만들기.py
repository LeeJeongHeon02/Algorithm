import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = []
result = []
visit1 = [[-1] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def BFS1(y, x, island): # 1단계
    q1 = deque()
    q1.append((y, x))
    visit1[y][x] = 0
    while q1:
        y, x = q1.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] == 1 and visit1[ny][nx] == -1:
                    visit1[ny][nx] = 0
                    graph[ny][nx] = island
                    q1.append((ny, nx))

def BFS2(island):
    visit = [[0] * N for _ in range(N)]
    q2 = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == island:
                q2.append((i, j))
                
    while q2:
        y, x = q2.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] == 0 and visit[ny][nx] == 0: #바다
                    visit[ny][nx] = visit[y][x] + 1
                    q2.append((ny, nx))
                if graph[ny][nx] != 0 and graph[ny][nx] != island: #땅
                    result.append(visit[y][x])
                    return
                    
island = 2
for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                graph[i][j] = island
                BFS1(i, j, island)
                island += 1
        
for k in range(2, island):
    BFS2(k)
    
print(min(result))