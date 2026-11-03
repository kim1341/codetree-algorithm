n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

drx,dry = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx,ny = i + drx[k], j +dry[k]
            if in_range(nx,ny) and grid[nx][ny] == 1:
                cnt +=1
        if cnt >= 3:
            ans +=1 
print(ans)