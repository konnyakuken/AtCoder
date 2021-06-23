N,X=map(int,input().split())
A=list(map(int,input().split()))
n=A.count(X)
for i in range(n):
    A.remove(X)
for i in range(N-n):
    print(A[i],end=" ")