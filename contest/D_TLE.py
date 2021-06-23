N,K=map(int,input().split())
A=list()
B=list()
ans=0
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    
for i in range(K):
    c=max(A)
    ans+=c
    l=A.index(c)
    A[l]-=B[l]
    if c==0:
        break
print(ans)