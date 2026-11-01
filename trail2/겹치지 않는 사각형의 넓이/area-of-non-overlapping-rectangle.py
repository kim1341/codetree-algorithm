x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

OFFSET = 1000
MAX_A = OFFSET *2+5
extent = [[0 for _ in range(MAX_A)] for _ in range(MAX_A)]

for i in range(3):
    x1[i]+=OFFSET
    x2[i]+=OFFSET
    y1[i]+=OFFSET
    y2[i]+=OFFSET
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            if i<2:
                extent[j][k] = 1
            else:
                extent[j][k] = 0
 

cnt = 0
for i in range(MAX_A):
    for j in range(MAX_A):
        cnt += extent[i][j]

print(cnt)
            