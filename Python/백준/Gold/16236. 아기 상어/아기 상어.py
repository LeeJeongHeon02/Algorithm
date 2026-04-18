import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
size = 2
stack = 0
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for j in range(n):
        if arr[j] == 9 : # 아기상어 위치 append
            q.append((i, j, 0)) # y, x, 시간
            graph[i][j] = 0

            
dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1] # 북 서 동 남
def BFS(q):
    global size, stack
    result = 0
    visit = [[0] * n for _ in range(n)]
    while q:
        lst = []
        for _ in range(len(q)):
            y, x, time = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    #근처 칸에 물고기 없거나 크기 같을때
                    if not visit[ny][nx] and (graph[ny][nx] == 0 or graph[ny][nx] == size):
                        q.append((ny, nx, time + 1))
                        visit[ny][nx] = 1
                    #근처 칸에 물고기 있을때(먹을수 있는), 큐 초기화 후 새로운 시작지점 설정
                    if 0 < graph[ny][nx] < size:
                        lst.append((ny, nx))
        if lst:
            q = deque()
            visit = [[0] * n for _ in range(n)]
            lst.sort(key = lambda x : (x[0], x[1]))
            q.append((lst[0][0], lst[0][1], time + 1))
            if stack + 1 == size:
                size += 1
                stack = 0
            else:
                stack += 1
            graph[lst[0][0]][lst[0][1]] = 0
            result = time + 1
    return result
print(BFS(q))