n, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dx, dy = [0,1,0,-1],[1,0,-1,0]

dir_num = 3
x,y = int(n/2), int(n/2)
result = board[x][y]
for dir in str:
    if dir == 'L':
        dir_num = (dir_num +3) % 4
    elif dir == 'R':
        dir_num = (dir_num +1) % 4
    else:
        nx, ny = x + dx[dir_num] , y + dy[dir_num]
        if not in_range(nx,ny):
            continue
        x,y = nx, ny
        result += board[x][y]


print(result)
