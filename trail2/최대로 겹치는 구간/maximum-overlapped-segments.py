n = int(input())
segment = [tuple(map(int,input().split())) for _ in range(n)]

arr = [0] *(n+205)

for a,b in segment:
    for i in range(a+100,b+100):
        arr[i]+=1

print(max(arr))