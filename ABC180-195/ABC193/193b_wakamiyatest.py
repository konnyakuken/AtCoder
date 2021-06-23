N=int(input())
ans=0
flag=0
for i in range(N):
    a,p,x=map(int,input().split())
    stock=x-a
    if(stock>0):
        if(flag==0):
            ans=p
            flag=1
        if(ans>p):
            ans=p

if(ans==0):
    print(-1)
else:    
    print(ans)