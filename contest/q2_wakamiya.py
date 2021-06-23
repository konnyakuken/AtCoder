N,M=map(int,input().split())
m=list()
for i in range(M):
    m.append(0)
A=list(map(int,input().split()))
count=0
for i in range(N):
    if (i+1)%M==0:
        count+=1
    m[(i+1)-(count*M)]+=A[i]
print(max(m))


