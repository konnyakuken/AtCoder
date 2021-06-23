N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=A[0]
b=B[0]
for i in range(N):
    if(a<=A[i]):#最大値
        a=A[i]
    if(b>=B[i]):#最小値
        b=B[i]

if((b-a)<0):
    print(0)
else:
    print(b-a+1)

