N,M,T=map(int,input().split())
N_max=N
BB=0
for i in range(M):
    A,B=map(int,input().split())
    C=B-A#カフェの時間
    N-=A-BB#カフェに行くまでの時間
    if 0>=N:
        print("No")
        break
    N+=C#充電
    BB=B#Bを保存
    if N>N_max:
        N=N_max
    if 0>=N:
        print("No")
        break
if N>0:
    N-=T-B
    if 0>=N:
        print("No")
    else:
        print("Yes")

