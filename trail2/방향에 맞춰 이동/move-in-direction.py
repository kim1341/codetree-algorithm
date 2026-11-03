n = int(input())
dir = []
move =[]
for i in range(n):
    d,m = input().split()
    dir.append(d)
    move.append(int(m))

dx,dy = [1,0,-1,0],[0,-1,0,1]
def diration(di):
    if di == 'E':
        return 0
    elif di =='S':
        return 1
    elif di=='W':
        return 2
    else:
        return 3
x,y= 0,0
for i in range(n):
    x,y = x + dx[diration(dir[i])]*move[i], y+ dy[diration(dir[i])]*move[i]


print(x,y)