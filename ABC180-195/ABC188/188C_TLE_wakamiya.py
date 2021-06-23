N=int(input())
A=list(map(int,input().split()))
player=dict()
n=2**N
for i in range(n):#辞書作成
    player[A[i]]=i+1
count=0
for i in range(N-1):
    for j in range(n):
        k=j*2
        if k>=n:
            break
        if A[k]>A[k+1]:
            A[k+1]=0
            count+=1
        else:
            A[k]=0
            count+=1
    for j in range(count):
            A.remove(0)
    n//=2
    count=0
if A[0]>A[1]:
    print(player[A[1]])
else:
    print(player[A[0]])