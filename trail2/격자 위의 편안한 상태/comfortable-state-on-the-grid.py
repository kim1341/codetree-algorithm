n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

arr = [[0 for _ in range(n)] for _ in range(n)]
result = [0] * (m)
#범위 체크
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

#격자
dxs,dys = [0,1,0,-1],[1,0,-1,0]

num = 0
#칸 칠하기
    #상하좌우 탐색
for a,b in points:
    r,c = a-1,b-1
    arr[r][c] = 1
    cnt = 0
    for i in range(4):
        nx, ny = r + dxs[i], c +dys[i]
        if in_range(nx,ny):
            if arr[nx][ny] == 1:
                cnt +=1
    if cnt == 3:
        result[num] = 1
    num+=1      

for ans in result:
    print(ans)