n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0 
result = 0
for i in range(n-1):
    if arr[i] == arr[i+1]:
        cnt += 1
    else:
        cnt = 0
    result = max(result,cnt)
print(result+1)