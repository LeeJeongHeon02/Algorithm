import sys
input = sys.stdin.readline
n = int(input().rstrip())
have_num = sorted(list(map(int, input().split())))
m = int(input().rstrip())
judge_num = list(map(int, input().split()))

result = []
def bi(k):
    left = 0
    right = len(have_num) - 1
    while left <= right:
        mid = (left + right) // 2
        if have_num[mid] == k:
            return 1
        if have_num[mid] > k:
            right = mid - 1
        else: # mid < k
            left = mid + 1
    return 0
for k in judge_num:
    result.append(bi(k))
    
print(' '. join(str(x) for x in result))