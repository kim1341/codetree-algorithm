N, K, P, T = map(int, input().split())
handshakes = [list(map(int, input().split())) for _ in range(T)]

num = [-1]* 101
num[P] = K
hand = sorted(handshakes)


for i in range(len(hand)):
    if  num[hand[i][1]] > 0 and num[hand[i][2]] >0:
        num[hand[i][1]] -=1
        num[hand[i][2]] -=1
    elif num[hand[i][1]]>0 and num[hand[i][2]] == -1:
        num[hand[i][1]] -=1
        num[hand[i][2]] = K
    elif num[hand[i][1]] == -1 and num[hand[i][2]] >0:
        num[hand[i][2]] -= 1
        num[hand[i][1]] = K  
    elif num[hand[i][1]] == 0 and num[hand[i][2]]>0:
        num[hand[i][2]] -=1
    elif num[hand[i][1]] >0 and num[hand[i][2]] == 0:
        num[hand[i][1]] -=1



for i in range(1,N+1):
    if  num[i]>=0:
        print(1,end="")
    else:
        print(0,end="")
