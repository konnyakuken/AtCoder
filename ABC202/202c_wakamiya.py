N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

count=[0]*N
num=0
for j in range(N):
    count[B[C[j]-1]-1]+=1
    #print(count)

for i in A:
    num+=count[i-1]

print(num)



