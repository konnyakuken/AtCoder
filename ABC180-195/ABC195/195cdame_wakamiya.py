N=int(input())
leng=len(str(N))
n=str(N)

ans=0
count=1
comma=0
a=0
for i in reversed(n):
    a+=count*int(i)
    count*=10
    if(count==1000):
        a+=1
        print(a)
        ans+=a*comma
        comma+=1
        a=0
        count=1
    
print(ans)


