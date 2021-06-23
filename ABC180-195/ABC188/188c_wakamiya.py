N=int(input())
A=list(map(int,input().split()))
player=dict()
n=2**N
for i in range(n):
    player[A[i]]=i+1
n//=2
for i in range(N-1):
    for j in range(n):
        if A[j]>A[j+1]:
            A.pop(j+1)
        else:
            A.pop(j)
    n//=2
if A[0]>A[1]:
    print(player[A[1]])
else:
    print(player[A[0]])