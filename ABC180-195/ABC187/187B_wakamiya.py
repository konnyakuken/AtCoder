N=int(input())
x=[]
y=[]
for i in range(N):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
count=0
for i in range(N):
    for j in range(i,N):
        n=3
        if x[j]-x[i] != 0 and i != j:
            n=(y[j]-y[i])/(x[j]-x[i])
        if n>=-1 and n<=1:
            count+=1
print(count)
