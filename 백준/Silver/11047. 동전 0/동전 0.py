n, k = map(int, input().split())

arr = []
answer = 0

for i in range(n):
    money = int(input())
    arr.append(money)

arr.sort(reverse = True)

for j in range(n):
    if k // arr[j] == 0:
        continue
    else:
        answer += k // arr[j]
        k = k - ((k // arr[j]) * arr[j])

print(answer)
