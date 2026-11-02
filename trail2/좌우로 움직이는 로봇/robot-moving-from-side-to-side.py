n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

MAX_T = 2000000+5
arr_a = [0] * MAX_T
arr_b = [0] * MAX_T
cnt = 0

cur, time = 0, 0
for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            cur -=1
        else:
            cur +=1
        time +=1
        arr_a[time] = cur

for i in range(time+1,MAX_T):
    arr_a[i] = cur

    
cur, time = 0, 0
for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            cur -=1
        else:
            cur +=1
        time +=1  
        arr_b[time] = cur
for i in range(time+1,MAX_T):
    arr_b[i] = cur

meet = True
for i in range(MAX_T):
    if arr_a[i] == arr_b[i]:
        if meet == False:
            cnt+=1
        meet = True
    else:
        meet = False

print(cnt)