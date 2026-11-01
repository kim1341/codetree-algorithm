n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

OFFSET = 100
MAX_A = OFFSET *2 + 5

area = [[0 for _ in range(MAX_A)] for _ in range(MAX_A)]

for i in range(n):
    x1 = OFFSET + x[i]
    y1 = OFFSET + y[i]
    x2 = x1 + 8
    y2 = y1 + 8
    for j in range(x1,x2):
        for k in range(y1,y2):
            area[j][k] = 1


sum_a =0
for i in range(MAX_A):
    for j in range(MAX_A):
        sum_a += area[i][j]

print(sum_a)