'''
16954 움직이는 미로 탈출
캐릭터는 visit 없이 8방향으로 모두 이동
캐릭터 먼저 이동 후 벽이내려옴
벽을 내리는 함수 따로 만들기.

벽이 사라지고, 캐릭터가 존재? - 도착가능
벽이 사라지고 캐릭터가 없음 - 도착불가능
'''
import sys
from collections import deque
index = sys.stdin.readline
graph = [['.'] * 8 for _ in range(8)]
q = deque()

for i in range(8):
    arr = list(input().rstrip())
    for j in range(8):
        if arr[j] == '#':
            graph[i][j] = '#'
            q.append((i, j))
graph[7][0] = 'c'

# 한 턴 벽 이동시키는 함수            
def down_wall():
    if not q:
        return False
    for i in range(len(q)):
        y, x = q.popleft()
        if y + 1 < 8:
            q.append((y + 1, x))
            graph[y + 1][x] = '#'
        graph[y][x] = '.'
    return True
        
dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
# 캐릭터 이동시키는 함수
def move(y, x, q2):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < 8 and 0 <= ny < 8 and graph[ny][nx] == '.':
            q2.append((ny, nx))
            #graph[ny][nx] = 'c'

while True:
    is_character = False
    q2 = deque()
    for i in range(8):
        for j in range(8):
            # move함수에서 만든 c가 다음 턴에 인식해야하는데 이번 턴에 바로 인식되어버리는 오류발생
            if graph[i][j] == 'c':
                is_character = True
                move(i, j, q2)
    while q2:
        a, b = q2.popleft()
        graph[a][b] = 'c'
                
    if not is_character:
        print(0)
        break
        
    if not down_wall() and is_character:
        print(1)
        break
        