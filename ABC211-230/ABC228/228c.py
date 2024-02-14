N,K = map(int,input().split())
score = []
for i in range(N):
    P1,P2,P3 = map(int,input().split())
    nowScore = sum([P1,P2,P3])
    score.append(nowScore)
sortScore = sorted(score,reverse=True)
for i in score:
    border = sortScore[K-1]
    if((border - i) <= 300 ):
        print("Yes")
    else:
        print("No")


