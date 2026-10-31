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

for i in range(n):
    b = a
    if dir[i] == 'L':
        b -= x[i]
    else:
        b += x[i] 

    for j in range(min(a,b),max(a,b)):
        arr[j] += 1
    
    a = b

for i in arr:
    if i >=2:
        cnt +=1

print(cnt)
