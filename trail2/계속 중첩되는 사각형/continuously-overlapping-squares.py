n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

OFFSET = 100
MAX_S = OFFSET *2 +5
area = [[0 for _ in range(MAX_S)] for _ in range(MAX_S)]
color = 1
for i in range(n):
    l1 = OFFSET +x1[i]
    m1 = OFFSET +y1[i]
    l2 = OFFSET +x2[i]
    m2 = OFFSET +y2[i] 
    for j in range(l1,l2):
        for k in range(m1,m2):
            if i % 2 == 0 :
                area[j][k] = 1
            elif i % 2 != 0:
                area[j][k] = 2

cnt = 0
for i in range(MAX_S):
    for j in range(MAX_S):
        if area[i][j] == 2:
            cnt +=1
print(cnt)