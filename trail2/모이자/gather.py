n = int(input())
A = list(map(int, input().split()))


result  = float('inf')

for i in range(n):
    distance = 0
    for j in range(n):
        distance = distance + A[j] * abs(i-j)
    result = min(distance,result)


print(result)