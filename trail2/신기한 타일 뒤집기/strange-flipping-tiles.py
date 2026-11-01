n = int(input())
command =[input().split() for _ in range(n)]
x= []
dir = []
for xi, diri in command:
    x.append(int(xi))
    dir.append(diri)

OFFSET = 100000
MAX_A = OFFSET * 2 + 5

arr_c = [""] * MAX_A
cnt_w,cnt_b = 0,0
a = OFFSET

for i in range(n):
    b = a
    if dir[i] == 'L':
        b -= x[i] -1
        for i in range(b,a+1):
            arr_c[i] = 'W'
    else:
        b += x[i] -1 
        for i in range(a,b+1):
            arr_c[i] = 'B'
    a = b

for i in arr_c:
    if i == 'W':
        cnt_w +=1
    elif i == 'B':
        cnt_b +=1

print(cnt_w,cnt_b)
