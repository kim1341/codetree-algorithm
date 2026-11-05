n = int(input())
grid = [[0] * n for _ in range(n)]


num = int((n-1)/2)
x,y = num,num
grid[x][y] = 1 
dxs, dys = [0,1,0,-1],[1,0,-1,0]
dir_num =0
step = 1
cnt = 0
for i in range(2,n*n+1):
    x,y = x+dxs[dir_num], y +dys[dir_num] 
    grid[x][y] = i

    cnt +=1
    if cnt == step:
        cnt = 0
        dir_num = (dir_num+3) %4
    
        if dir_num %2 ==  0:
            step +=1


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()