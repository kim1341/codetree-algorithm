dirs = input()

dx,dy =[0,1,0,-1],[1,0,-1,0]

x,y,d = 0,0,0
for i in dirs:
    if i =='L':
        d = (d+3) % 4
    elif i =='R':
        d = (d+1) % 4
    else:
        x = x+dx[d]
        y = y+dy[d]

print(x,y)
        
        
        