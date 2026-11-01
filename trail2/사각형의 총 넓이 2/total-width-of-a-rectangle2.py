n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

OFFSET = 1000
MAX_A = OFFSET * 2 + 5
extent = [[0 for _ in range(MAX_A)] for _ in range(MAX_A)]

for i in range(n):
    for j in range(x1[i]+OFFSET,x2[i]+OFFSET):
        for k in range(y1[i]+OFFSET,y2[i]+OFFSET):
            extent[j][k] = 1
    
cnt = 0
for i in range(MAX_A):
    for j in range(MAX_A):
        cnt += extent[i][j]

print(cnt)