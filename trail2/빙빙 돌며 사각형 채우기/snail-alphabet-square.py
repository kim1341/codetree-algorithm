n, m = map(int, input().split())

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

dxs, dys = [0,1,0,-1],[1,0,-1,0]

arr = [[" " for _ in range(m)]for _ in range(n)]
x,y = 0,0
a = 65
arr[x][y] = chr(a)
dir_num = 0
for i in range(1,n*m):
    nx,ny = x + dxs[dir_num] , y +dys[dir_num]
    if not in_range(nx,ny) or arr[nx][ny] != " ":
        dir_num = (dir_num+1)%4
    x,y = x+dxs[dir_num], y + dys[dir_num]
    a  = chr(65+i %26)
    arr[x][y] =a

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
