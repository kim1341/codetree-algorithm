n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

MAX_T = 1000000
arr_a =[0] * MAX_T
arr_b =[0] * MAX_T

num = 0
for i in range(n):
    for j in range(1,t[i]+1):
        if num>0:
            arr_a[num] = arr_a[num-1] + v[i]
        else:
            arr_a[num] = v[i]
        num += 1

num = 0
for i in range(m):
    for j in range(1,t2[i]+1):
        if num>0:
            arr_b[num] = arr_b[num-1] + v2[i]
        else:
            arr_b[num] = v2[i]
        num += 1


leader = 0
cnt = 0

for i in range(MAX_T):
    if arr_a[i]>arr_b[i]:
        if leader == 2:
            cnt +=1
        leader = 1
    elif arr_a[i]< arr_b[i]:
        if leader == 1:
            cnt +=1
        leader = 2

print(cnt)