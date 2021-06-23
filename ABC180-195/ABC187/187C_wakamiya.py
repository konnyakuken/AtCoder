N=int(input())#TLE,WAあり
x=[]
flag=0
for i in range(N):
    a=input()
    x.append(a)

for i in range(N):
    if x[i][:1]=="!":
        check=x[i].lstrip("!")
    elif flag==1:
        break
    else:
        check="!"+x[i]
    
    for j in range(i,N):
        if check==x[j]:
            ans=x[j]
            flag=1
            break
        
if flag==0:
    print("satisfiable")
else:
     if ans[:1]=="!":
        ans=ans.lstrip("!")
        print(ans)
