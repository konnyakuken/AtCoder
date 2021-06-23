H,W=map(int,input().split())
mas=[]
ans=0
for i in range(H):
    n=list(map(int,input().split()))
    mas.extend(n)

minmin=min(mas)
for i in mas:
    ans+=i-minmin
print(ans)
