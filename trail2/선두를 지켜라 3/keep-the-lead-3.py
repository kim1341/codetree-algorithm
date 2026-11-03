N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

arr_a = [0]*(sum(t)+1)
arr_b = [0]*(sum(t2)+1)
timeA = 1
for i in range(N):
    for j in range(1,t[i]+1):
        arr_a[timeA] = v[i] +arr_a[timeA-1]
        timeA+=1


timeB = 1
for i in range(M):
    for j in range(1,t2[i]+1):
        arr_b[timeB] = v2[i] +arr_b[timeB-1]
        timeB+=1

total = max(timeA,timeB) -1

leader,cnt = 0,0
for i in range(1,timeA):
    if arr_a[i]>arr_b[i]:
        if leader !=1:
            cnt +=1
        leader =1
    elif arr_a[i]<arr_b[i]:
        if leader !=2:
            cnt +=1
        leader =2
    else:
        if leader !=3:
            cnt +=1
        leader =3

print(cnt)