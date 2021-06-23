N=int(input())
A=list(map(int,input().split()))
M=0
sum=0
sum_M=0
flag=0
for i in range(N):
    if A[i]>=M:
            M=A[i]
            flag=1
    if flag==1:
        for j in range(i,N):
            if A[j]>=M:
                sum+=M
            else:
                if sum>=sum_M:
                    sum_M=sum
                sum=0
                flag=0
                break
    if sum>=sum_M:
        sum_M=sum
    sum=0
    flag=0
print(sum_M)