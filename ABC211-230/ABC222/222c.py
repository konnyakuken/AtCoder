def RockPaperScissors (A,B,A_num,B_num):
    #文字列GCPをそれぞれintに変換
    A = Janken.index(A)
    B = Janken.index(B)
    if(A == B):#あいこ
        return
    elif((A == 0 and B == 1)or(A == 1 and B == 2)or(A == 2 and B == 0)):
        score[A_num][1]+=1
    else:
        score[B_num][1]+=1

N,M = map(int,input().split())
A = list()
score = list()
now_score = list()
Janken= ["G","C","P"]

for i in range(2*N):
    A.append(list(input()))
    score.append([i+1,0])

for m in range(M):
    #初回
    if (m == 0):
        for n in range(N):
            RockPaperScissors(A[2*n][m],A[2*n+1][m],2*n,2*n+1)
    else:
        for k in range(N):
           #nowScoreが1からなので配列参照できるように最後に−1
           A_num = now_score[2*(k+1)-2][0] -1
           B_num = now_score[2*(k+1)-1][0] -1
           RockPaperScissors(A[[A_num][0]][m],A[B_num][m],A_num,B_num)
    #ソートをしたものを毎回用意
    now_score = sorted(score,reverse=True, key=lambda x:x[1])
    
for i in now_score:
    print(i[0])




