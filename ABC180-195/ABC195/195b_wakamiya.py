A,B,W=map(int,input().split())#WAあり
W*=1000

ans=[]
for i in range(1,1000*100+1):
    if (A*i<=W and W<=B*i):
        ans.append(i)

if (len(ans)!=0):
    print(min(ans),max(ans))
else:
    print("UNSATISFIABLE")

