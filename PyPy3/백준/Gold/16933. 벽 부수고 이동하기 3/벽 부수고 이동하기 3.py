import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split()) # N = y, M = x
graph = []
visit = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def BFS():
    move = 1
    q = deque()
    q.append((0, 0, True, K, move))
    visit[K][0][0] = 1
    while q:
        y, x, day, k, m = q.popleft()
        if x == M - 1 and y == N - 1:
            return m
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                # 일반적인경우
                if not visit[k][ny][nx] and graph[ny][nx] == 0:
                    visit[k][ny][nx] = 1
                    q.append((ny, nx, not day, k, m + 1))
                    
                if k > 0 and graph[ny][nx] == 1 and not visit[k - 1][ny][nx]:
                    if day: # 벽부쉬고 갈수있는경우
                        visit[k - 1][ny][nx] = 1
                        q.append((ny, nx, not day, k - 1, m + 1))
                    else: # 제자리에 있는경우
                        q.append((y, x, not day, k, m + 1))
    return -1
print(BFS())