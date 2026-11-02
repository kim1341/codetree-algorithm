N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]


ans = -1

penalty= [0]*(N+1)
#k번 벌칙을 받은 사람을 구하기
for i in student:
    penalty[i] = penalty[i] + 1
    if penalty[i] == K:
        ans = i
        break

print(ans)
    

