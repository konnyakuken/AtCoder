N=int(input())
leng=len(str(N))

n=str(N)

ans=0
count=0
comma=0
a=0
if leng>3:
    while True:
        leng-=3
        
        if leng==0:
            
            break
        elif leng<3:
            count+=1
            break
        count+=1
        




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


