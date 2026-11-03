n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

mapper ={
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

dxs,dys = [0,1,-1,0],[1,0,0,-1]

def in_range(x,y):
    return 1<=x and x<=n and 1<=y and y<=n
move = mapper[d]
time = 0
x, y = r,c
while time < t:
    x,y = x +dxs[move], y + dys[move]
    if not in_range(x,y):
        x,y = x -dxs[move], y -dys[move]
        move = 3- move
    time+=1
print(x,y)


