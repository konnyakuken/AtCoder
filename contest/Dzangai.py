def cal():
    max_num = 0
    count=0
    for i in A:
        if max_num < i:
            max_num = i
        count+=1
    return max_num,count
    

N,K=map(int,input().split())
A=list()
B=list()
ans=0
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    
for i in range(K):
    c,count=cal()
    ans+=c
    A[count-1]-=B[count-1]
    if c==0:
        break
print(ans)