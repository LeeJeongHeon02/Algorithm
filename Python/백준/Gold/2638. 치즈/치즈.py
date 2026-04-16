import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) #y, x
graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
def BFS(a, b, c):
    q = deque()
    q.append((a, b))
    visit = [[0] * m for _ in range(n)]
    visit[a][b] = 1
    graph[a][b] = c
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx]:
                if graph[ny][nx] == 0 or graph[ny][nx] == 2:
                    visit[ny][nx] = 1
                    graph[ny][nx] = c
                    q.append((ny, nx))
    return visit
while True:
    visit = BFS(0, 0, 0)
    is_continue = False
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visit[i][j] and graph[i][j] == 0:
                BFS(i, j, 2)          
    #공기랑 두 변 이상 접촉된 치즈 삭제            
    delq = deque()            
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] == 1:
                is_continue = True
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if not graph[ny][nx]:
                        cnt += 1
                        if cnt >= 2:
                            delq.append((i, j))
                            break
    while delq:
        y, x = delq.popleft()
        graph[y][x] = 0
    if not is_continue:
        break
    answer += 1
print(answer)