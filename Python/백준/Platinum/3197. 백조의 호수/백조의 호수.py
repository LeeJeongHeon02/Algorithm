import sys
from collections import deque
input = sys.stdin.readline


R, C = map(int, input().split()) # R = y, C = x
graph = []
visit = [[0] * C for _ in range(R)]
duck = [] # 백조 두마리의 위치 
q1 = deque() # 첫 백조의 위치
q2 = deque() # 물 공간(L + .)의 좌표 저장
for i in range(R):
    arr = list(map(str, input().rstrip()))
    graph.append(arr)
    for j in range(C):
        if arr[j] == "L":
            duck.append((i, j))
        if arr[j] != "X":
            q2.append((i, j))
            

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visit1 = [[0] * C for _ in range(R)]
q1.append(duck[0])
duck_x, duck_y = duck[1][1], duck[1][0]
visit1[duck[0][0]][duck[0][1]] = 1

def duckBFS():
    q3 = deque()
    while q1:
        y, x = q1.popleft()
        if x == duck_x and y == duck_y:
            return (True, 1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and not visit1[ny][nx]:
                if graph[ny][nx] == "X": #다음턴의 백조의 위치
                    q3.append((ny, nx))
                else:
                    q1.append((ny, nx))
                visit1[ny][nx] = 1

    return (False, q3)

def meltBFS():
    global q2
    q4 = deque()
    while q2:
        y, x = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == "X":
                q4.append((ny, nx))
                graph[ny][nx] = "."
    return q4
    
answer = 0
while True:
    result1 = duckBFS()
    if result1[0]:
        print(answer)
        break
    else:
        q1 = result1[1]
        q2 = meltBFS()
    answer += 1