n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

#범위
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dxs,dys = [1,0,-1,0],[0,-1,0,1]
#방향 정보
dir = [0] * (n*4)
dir_num = 0
num = 0
while num < n*4:
    dir[num] = dir_num

    if (num+1) %n == 0:
        dir_num +=1

    num+=1

p = k-1
cnt = 0
range = True
x,y = 0,0
pos = p % n
if dir[p] == 0:
    x,y = 0, pos
elif dir[p] == 1:
    x,y = pos,n-1
elif dir[p] == 2:
    x,y = n-1,n-1-pos
else:
    x,y = n-1-pos,0
move_num = dir[p]

while range:

    if move_num == 0:
        if grid[x][y] == '/':
            move_num = 1
        else:
            move_num = 3
    elif move_num == 1:
        if grid[x][y] == '/':
            move_num = 0
        else:
            move_num = 2
    elif move_num == 2:
        if grid[x][y] =='/':
           move_num = 3
        else:
            move_num = 1
    else:
        if grid[x][y] == '/':
            move_num = 2
        else:
            move_num = 0 

    nx,ny = x+dxs[move_num], y+dys[move_num]
    if not in_range(nx,ny):
        range = False
    x,y = nx,ny
    cnt+=1

print(cnt)
