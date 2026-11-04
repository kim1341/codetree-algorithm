N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

ans = -1

mapper ={
    'E':0,
    'S':1,
    'W':2,
    'N':3
}
dx,dy = [1,0,-1,0],[0,-1,0,1]
x,y,time =0, 0, 0
result = False
for i in range(N):
    for j in range(dist[i]):
        x, y = x +dx[mapper[dir[i]]], y +dy[mapper[dir[i]]]
        time +=1
        if x == 0 and y ==0:
            result = True
            break
    if result:
        ans = time
        break
print(ans)
