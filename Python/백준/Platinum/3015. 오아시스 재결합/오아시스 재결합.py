import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack = []
arr = [0] * n
answer = 0
for i in range(n):
    arr[i] = int(input().rstrip())
for j in arr:
    while stack and stack[-1][0] < j:
        stack.pop()
        answer += 1
    if stack and stack[-1][0] == j:
        maxnum = max(stack[0])
        if maxnum == j:
            answer += stack[-1][1]
            stack.append((j, stack[-1][1] + 1))
        else:
            answer += stack[-1][1] + 1
            stack.append((j, stack[-1][1] + 1))
    elif stack and stack[-1][0] > j:
        answer += 1
        stack.append((j, 1))
    else:
        stack.append((j, 1))

print(answer)