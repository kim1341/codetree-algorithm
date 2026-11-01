x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

OFFSET = 1000
MAX_S = OFFSET *2 +5

area = [[0 for _ in range(MAX_S)] for _ in range(MAX_S)]
a = 1
#사각형 칠하기
for i in range(2):
    l1 = x1[i] + OFFSET
    m1 = y1[i] + OFFSET
    l2 = x2[i] + OFFSET
    m2 = y2[i] + OFFSET
    for j in range(l1,l2):
        for k in range(m1,m2):
            area[j][k] = a
    a +=1


#최대 행열, 최소 행열 좌표 구하기
max_l,max_m,min_l,min_m = 0,0,MAX_S,MAX_S

for i in range(MAX_S):
    for j in range(MAX_S):
        if area[i][j] == 1:
            max_l = max(max_l,i)
            max_m = max(max_m,j)
            min_l = min(min_l,i)
            min_m = min(min_m,j)
if max_l== 0 and max_m == 0 and min_l== MAX_S and min_m == MAX_S:
    print(0)
else:
    print((max_l-min_l+1)*(max_m-min_m+1))