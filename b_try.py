N=int(input())
a=list(map(int,input().split()))
a.sort()

ans=0


for i in range(N):
    for j in range(i+1,N):
        for z in range(j+1,N):
            #print(a[i],a[j],a[z])
            if (a[i]!=a[j] and a[j]!=a[z] and a[i]!=a[z]) and (a[i]+a[j]>a[z]):
            #if not(a[i]==a[j] and a[j]==a[z] and a[i]==a[z])and (a[i]+a[j]>a[z]):
                ans=ans+1
                #print("oooooooo{},{},{}".format(i,j+1,z+1))
                           
print(ans)

