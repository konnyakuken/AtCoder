N,M=map(int,input().split())
n=list()
for i in range(N):
    n.append(i+1)
v=list(map(int,input().split()))
ans=set(n)^set(v)
if ans:
    for i in ans:
        print(i,end=" ")
else:
    print(-1)
