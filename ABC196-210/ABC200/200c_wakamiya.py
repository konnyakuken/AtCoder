
import sys
input = sys.stdin.readline
import itertools 

N=int(input())
A=list(map(int,input().split()))

#B=itertools.combinations(A,2)
count=0
num=0
for i in A:
    num+=1
    for j in A[num:]:
        if((i-j)%200==0):
            count+=1
print(count)