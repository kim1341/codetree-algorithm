n, m = map(int,input().split())
d = []
x = []
for _ in range(n):
    a,b = input().split()
    d.append(a)
    x.append(int(b))
d2 =[]
x2 =[]
for _ in range(m):
    a2,b2 = input().split()
    d2.append(a2)
    x2.append(int(b2))

sec = sum(x)+5

arr_a = [0] * sec
arr_b = [0] * sec
cur_a, cur_b = 0, 0
start = 0
for i in range(n):
    end = start + x[i]
    for j in range(start+1,end+1):
        if d[i] == 'L':
            cur_a -=1
        else:
            cur_a +=1
        arr_a[j] = cur_a
    start = end 

start = 0
for i in range(m):
    end = start + x2[i]
    for j in range(start+1,end+1):
        if d2[i] == 'L':
            cur_b -=1
        else:
            cur_b +=1
        arr_b[j] = cur_b
    start = end

ans = -1
for i in range(sum(x)+1):
    if i> 0 and arr_a[i] == arr_b[i]:
        ans = i
        break


print(ans)