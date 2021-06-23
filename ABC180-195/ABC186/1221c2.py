N=int(input())
unlucky10=[]
unlucky8=[]
for i in range(N+1):
    n=str(i)    
    if (n.find("7")==-1):
        unlucky10.append(int(n))

for i in range(N+1):    
    n=(oct(i))
    #print(type(n))
    if (n.find("7")==-1):
        unlucky8.append(int(n[2:],8))#0oの次から
#print(unlucky10)
#print(unlucky8)
s10=set(unlucky10)#集合にする
s8=set(unlucky8)
s=s10 & s8#積集合
ans=list(s)
#print(ans)
print((len(ans)-1))#0を含まない
          