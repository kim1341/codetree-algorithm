commands = input()

dx, dy = [1,0,-1,0],[0,-1,0,1]

time = 0
x,y = 0,0
ans = -1
dir_num = 3

#시간, 움직임
for dir in commands:
    if dir =='F':
        x, y = x + dx[dir_num], y +dy[dir_num]
    elif dir == 'R':
        dir_num = (dir_num+1)%4
    else:
        dir_num = (dir_num +3)%4
    time +=1

    if x == 0 and y == 0:
        ans = time
        break

print(ans)


