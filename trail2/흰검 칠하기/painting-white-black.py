n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)


OFFSET = 100000
MAX_S = OFFSET*2+5
arr_w = [0] * MAX_S
arr_b = [0] * MAX_S
arr_c = [""]* MAX_S
a = OFFSET
cnt_w,cnt_b,cnt_g = 0,0,0

for i in range(n):
    b = a
    if dir[i] == 'L':
        b -= x[i] -1
        for j in range(b,a+1):
            arr_w[j] +=1
            arr_c[j] = 'W'
        
    else:
        b += x[i]-1
        for j in range(a,b+1):
            arr_b[j] +=1
            arr_c[j] ='B'
    a = b

for i in range(MAX_S):
    if arr_w[i] >=2 and arr_b[i]>=2:
        cnt_g+=1
    elif arr_c[i] == 'W':
        cnt_w+=1
    elif arr_c[i] == 'B':
        cnt_b+=1
print(cnt_w,cnt_b,cnt_g)