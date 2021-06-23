N,X=map(int,input().split())
V=[]
P=[]
sum=0
flag=0
for i in range(N):
    a,b=map(int,input().split())
    V.append(a)
    P.append(b)
for i in range(N):
    alcohol=V[i]*P[i]#普通に割ると小数点以下で誤差発生
    sum+=alcohol
    if sum>X*100:
        print(i+1)
        flag=1
        break
if flag==0:
    print(-1)