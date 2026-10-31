OFFSET = 1000
MAX_A = 2000
n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr =[0]*(MAX_A+5)
cnt = 0
a = OFFSET
if dir[0] == 'L': 
    b = OFFSET - x[0]
else:
    b = OFFSET + x[0]
for i in range(n):
    
    if dir[i] == 'L':
        for j in range(b,a):
            arr[j] +=1
    else:
        for j in range(a,b):
            arr[j] +=1
    

    if i != n-1:
        a = b
        if dir[i+1] == "L":
            b = b - x[i+1]
        else:
            b = b + x[i+1]

for i in arr:
    if i >=2:
        cnt +=1

print(cnt)
